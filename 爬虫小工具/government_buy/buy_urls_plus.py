import requests
import random
from datetime import datetime, timedelta
from chardet import detect
import time

def get_request_headers(referer=None):
    """生成随机请求头，模拟浏览器访问"""
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
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    return headers


def get_ccgp_text(page,kw):
    """访问政府采购网搜索页面并返回页面文本内容"""
    url = 'http://search.ccgp.gov.cn/bxsearch?'

    # 计算近30天的日期范围
    curr_date = datetime.now()
    start_date = curr_date - timedelta(days=30)
    start_time = start_date.strftime("%Y:%m:%d")
    end_time = curr_date.strftime("%Y:%m:%d")

    # 构造请求参数（搜索关键词为“等级保护”，区域为山西）
    params = {
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

    # 获取请求头
    headers = get_request_headers()

    try:
        # 发送请求（添加随机延迟避免被拦截）
        time.sleep(random.randint(2, 6))
        response = requests.get(url, headers=headers, params=params, allow_redirects=True)
        response.raise_for_status()  # 检查请求是否成功

        # 自动检测编码并解码
        encoding = detect(response.content).get('encoding', 'utf-8')
        page_text = response.content.decode(encoding)

        return page_text

    except Exception as e:
        print(f"请求失败：{str(e)}")
        return None


# 执行并打印结果
if __name__ == "__main__":
    keyword = input('关键词：')
    pg = input('页数：')

    page_content = get_ccgp_text(page=pg,kw=keyword)
    if page_content:
        print("页面文本内容：")
        print(page_content)