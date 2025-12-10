import requests
from PIL import Image
import io

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'content-length': '0',
    'origin': 'https://www.zhipin.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zhipin.com/sem/10.html?_ts=1748928745421&sid=sem_bingpc&qudao=bing_pc_H120003UY5&plan=BOSS-%E5%BF%85%E5%BA%94-%E5%93%81%E7%89%8C&unit=%E7%B2%BE%E5%87%86&keyword=boss%E7%9B%B4%E8%81%98&msclkid=74a082f5db7a1ab6c9a5eacb53c48a58',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': 'F-47b0f9XaULUibOkT',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    # 'cookie': 'ab_guid=c456c365-067c-45e5-b9c0-cac931b30e81; __zp_stoken__=e01efw5LDiMSBY0dkFRtqZWt3WFNXwr9Zc8K9w4zDiVhnw4thwq9mwr9twrJQTnHCklFbUVV4wpdUwrvCr8O%2Fw4zCj8Ktwr1YwpfDhcKYw4TEiMOHwrPDhcK3w4jDrcKuw6pOwqzDiMKQWMOrwq3CkMKkxYnDgcOvwq3FhMKfxIbDjMWJwrHEu8OKw7PCvsOnxIXFh8Kkw6rDucOPwo7DqsO8xKrCrsObxa3EocKpxb7EqcWMw4vCnkY1EhYWFg0bDw8PGBYSFRUOERUVFQ4TFxcXEEQvxIvDknxCRUJLMlhUVBlWZ15bXlINaFxaREMODmJeQzFLS0Q%2Fw4FLw4jCtMOFS8OIwrvDij%2FDiMSLS0w%2FS8OGw6wvMMOLw5YXw4TEgRfDhsOLEMK%2FxYkXw4vCsGTDm2PCicOLxITDhcOtKj5Bw4vFjEI9HUFGRktCRkNGPS1Fw4vDi8OUZ8KJw4TEiMK%2Bw6U2SyZFQkY9SD1CRj9GSy5GPhUzQks7Qg4XFhYULkXDh8Krw4vDp0JG; lastCity=101270100; __g=sem_bingpc; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1748586537,1748594915,1748927019,1748928706; HMACCOUNT=F4026F981A65044E; __zp_seo_uuid__=7eb476a8-3beb-469f-9f54-51e71591cd17; __c=1748928706; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1748928745421%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3D74a082f5db7a1ab6c9a5eacb53c48a58&s=1&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1748928745421%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3D74a082f5db7a1ab6c9a5eacb53c48a58&s=3&friend_source=0; __a=36300358.1748586537.1748927019.1748928706.46.4.3.3; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1748928746',
}

def get_details():
    """
    {
        'code': 0,
        'message': 'Success',
        'zpData': {
            'qrId': 'bosszp-b540a19e-d52f-49f5-9e61-763eea7a674e',
            'randKey': 'EuhFFcC7t6iHyUZhaWonQZswn6Yxfe78',
            'secretKey': 'UHqGmn3D',
            'shortRandKey': 'bosszp-aFfZesZF7d5Q8QbU'
        }
    }
    """
    response = requests.post('https://www.zhipin.com/wapi/zppassport/captcha/randkey', headers=headers)
    return response.json()

def get_qr(ct):
    params = {
        'content': ct,
        'w': '200',
        'h': '200',
    }
    response = requests.get('https://www.zhipin.com/wapi/zpweixin/qrcode/getqrcode', params=params, headers=headers)
    img = Image.open(io.BytesIO(response.content))
    img.show()
    # 给前端
    return response.content

def get_scan(ct):
    params = {
        'uuid':ct,
    }
    response = requests.get('https://www.zhipin.com/wapi/zppassport/qrcode/scan', params=params,headers=headers)
    return response.json()

if __name__ == '__main__':
    qrId = get_details()['zpData']['qrId']
    print(get_qr(qrId))
    print(get_scan(qrId))