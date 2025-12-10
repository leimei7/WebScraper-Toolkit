import time
import random
import re
import requests
import urllib3
import base64
from flask import Flask, jsonify
from flask_cors import CORS  # 引入 flask - cors
from threading import Thread

from get_code import get_authorization_url
from get_key import post_request

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 全局变量
session2 = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}
app = Flask(__name__)
CORS(app, origins="http://localhost:63342")  # 配置允许的源

login_status = {'success': False, 'message': ''}
pt_login_sig = None
ptqrtoken = None

def final_final(cookies):
    params = ['p_skey', 'pt4_token', 'pt_oauth_token', 'p_uin']
    extracted_params = {}

    # 遍历 cookies 提取所需参数
    for cookie in cookies:
        if cookie.name in params:
            extracted_params[cookie.name] = cookie.value

    # 输出提取的参数
    for param, value in extracted_params.items():
        print(f"{param}: {value}")

    p_skey = extracted_params.get('p_skey')
    pt4_token = extracted_params.get('pt4_token')
    pt_oauth_token = extracted_params.get('pt_oauth_token')
    p_uin = extracted_params.get('p_uin')
    g_tk = calculate_g_tk(p_skey)
    code = get_authorization_url(p_skey, pt4_token, pt_oauth_token, p_uin, g_tk)
    m_key = post_request(g_tk, code)
    return m_key

def calculate_g_tk(skey):
    n = 5381
    for c in skey:
        n += (n << 5) + ord(c)
    return n & 2147483647


def decryptQrsig(qrsig):
    e = 0
    for c in qrsig:
        e += (e << 5) + ord(c)
    return 2147483647 & e


def init_session2():
    global session2
    session2 = requests.Session()
    session2.headers.update(headers)


def get_pt_login_sig():
    xlogin_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?'
    params = {
        'appid': '716027609',
        'daid': '383',
        'style': '33',
        'login_text': '授权并登录',
        'hide_title_bar': '1',
        'hide_border': '1',
        'target': 'self',
        's_url': 'https://graph.qq.com/oauth2.0/login_jump',
        'pt_3rd_aid': '100497308',
        'pt_feedback_link': 'https://support.qq.com/products/77942?customInfo=.appid100497308',
    }
    response = session2.get(xlogin_url, params=params)
    return session2.cookies.get('pt_login_sig')


def get_qrcode():
    global pt_login_sig, ptqrtoken
    ptqrshow_url = 'https://ssl.ptlogin2.qq.com/ptqrshow?'
    params = {
        'appid': '716027609',
        'e': '2',
        'l': 'M',
        's': '3',
        'd': '72',
        'v': '4',
        't': str(random.random()),
        'daid': '383',
        'pt_3rd_aid': '100497308',
    }
    response = session2.get(ptqrshow_url, params=params)
    qr_code_base64 = base64.b64encode(response.content).decode('utf-8')
    qrsig = session2.cookies.get('qrsig')
    ptqrtoken = decryptQrsig(qrsig)
    return qr_code_base64


def check_qrcode_status():
    global login_status, session2
    ptqrlogin_url = 'https://ssl.ptlogin2.qq.com/ptqrlogin?'
    while True:
        params = {
            'u1': 'https://graph.qq.com/oauth2.0/login_jump',
            'ptqrtoken': ptqrtoken,
            'ptredirect': '0',
            'h': '1',
            't': '1',
            'g': '1',
            'from_ui': '1',
            'ptlang': '2052',
            'action': '0-0-%s' % int(time.time() * 1000),
            'js_ver': '20102616',
            'js_type': '1',
            'login_sig': pt_login_sig,
            'pt_uistyle': '40',
            'aid': '716027609',
            'daid': '383',
            'pt_3rd_aid': '100497308',
            'has_onekey': '1',
        }
        response = session2.get(ptqrlogin_url, params=params)
        print(response.text)
        if '二维码未失效' in response.text or 'дЇМзїіз†БиЃ§иѓБдЄ≠гАВ' in response.text:
            login_status = {'success': False, 'message': '等待登录'}
        elif '二维码已经失效' in response.text:
            login_status = {'success': False, 'message': '二维码已经失效'}
            break
        elif "成功" in response.text:
            login_status = {'success': True, 'message': '登录成功'}
            # 调用 finalize_login 完成最终登录
            final_session2 = finalize_login(response)

            mkey = final_final(final_session2.cookies)
            print(mkey)
            break
        else:
            login_status = {'success': False, 'message': '登录失败'}
            break
        time.sleep(2)


def finalize_login(response):
    qq_number = re.findall(r'&uin=(.+?)&service', response.text)[0]
    url_refresh = re.findall(r"'(https:.*?)'", response.text)[0]
    response1 = session2.get(url_refresh, allow_redirects=False, verify=False)
    print('账号「%s」登陆成功' % qq_number)
    return response1


@app.route('/newlogin/qrcode/')
def newlogin_qrcode():
    global pt_login_sig, login_status
    login_status = {'success': False, 'message': ''}
    init_session2()
    pt_login_sig = get_pt_login_sig()
    qr_code_base64 = get_qrcode()
    thread = Thread(target=check_qrcode_status)
    thread.start()
    return jsonify({'qr_code_base64': qr_code_base64})


@app.route('/newlogin/check_status/')
def newlogin_check_status():
    global login_status
    return jsonify(login_status)


if __name__ == '__main__':
    app.run(debug=True)