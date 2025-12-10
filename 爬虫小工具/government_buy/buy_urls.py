import random
import re
import time
import requests
from datetime import datetime

from buy_datas import extract_content

def get_param(page,kw):
    param = {
        'searchtype': '1',
        'page_index': page,
        'bidSort': '0',
        'buyerName': '',
        'projectId': '',
        'pinMu': '0',
        # 7是中标，0为所
        'bidType': '7',
        'dbselect': 'bidx',
        'kw': kw,
        # 可修改时间
        # 'start_time': '2025:06:20',
        # 'end_time': '2025:06:28',
        # 'end_time': str(datetime.now().strftime("%Y:%m:%d")),
        'timeType': '2',
        'displayZone': '',
        'zoneId': '',
        'pppStatus': '0',
        'agentName': '',
    }
    return param

def get_headers(referer=None):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
    ]
    ua = random.choice(user_agents)
    headers = {
        "User-Agent": ua,
        "Host": "search.ccgp.gov.cn",
        "Referer": referer if referer else "http://search.ccgp.gov.cn/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",  # 修正连字符格式
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    return headers

def tool(url,param=None,refer=None):
    headers = get_headers(refer)
    # 休息时间
    time.sleep(random.randint(2,6))
    response = requests.get(url, headers=headers, params=param,  allow_redirects=True)
    # print("main_url:",response.url)
    # 服务器返回异常页面
    if 200 != response.status_code :
        print("main_url:",response.url)
        print('Response Status Code: ' + str(response.status_code))
        print()
    return response

def get_detail_url(htm):
    pattern = r'var ohtmlurls="([^"]+)"'
    match = re.search(pattern, htm)
    i = 1
    if match:
        ohtmlurls_value = match.group(1)
        url_array = ohtmlurls_value.split(',')

        # 移除可能存在的空字符串元素（如果原字符串末尾有逗号）
        url_array = [url for url in url_array if url]

        # 替换协议
        url_array = [url.replace('http', 'https') for url in url_array]

        # 打印数组元素个数和前几个元素示例
        print(f"共解析出 {len(url_array)} 个URL")
        for url in url_array:
            print(i,url)
            i = i + 1
        # 返回
        return url_array
    else:
        print("未找到ohtmlurls的值")
        return None

def get_datas(urls:list):
    results = []
    if urls:
        for url in urls:
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
            ]
            ua = random.choice(user_agents)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'User-Agent': ua
            }
            time.sleep(random.randint(2, 6))
            response = requests.get(
                url,
                headers=headers,
            )
            response.encoding = 'utf-8'
            results.append(extract_content(response.text))
            print("爬取中......")
        return results
    else:
        return None


base_url = 'http://search.ccgp.gov.cn/bxsearch'

if __name__ == '__main__':
    keyword = input('关键词：')
    pg = input('页数：')
    res = tool(base_url,get_param(pg,keyword))
    html_content = res.text
    datas_array = get_datas(get_detail_url(html_content))
    if datas_array:
        filename = f"{keyword}第{pg}页共{len(datas_array)}条.csv"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for data in datas_array:
                    file.write(data + '\n')
            print(f"数据已成功保存到 {filename}")
        except Exception as e:
            print(f"保存文件时出错: {e}")
    else:
        print("None")