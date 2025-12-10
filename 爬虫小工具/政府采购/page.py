import requests
import re

#ip池

cookies = {
    'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1748586074',
    'HMACCOUNT': 'F4026F981A65044E',
    'HMF_CI': 'be3cb6eb91ef0a81f68cc494e55a00b380880e2bf19923df62dca68c903a3537c81cbe8e72f564d5645ee6c1423c12cd8a574a71639096678700da37fd05b48840',
    'Hm_lvt_9459d8c503dd3c37b526898ff5aacadd': '1748586076',
    'JSESSIONID': '-RUgSMh2tKrnaAlZpvwftk5Oop59tX0g1Ng9nzkqbfBH9uySl8HS!485428781',
    'HMY_JC': '07fe7b45ebcd1eedcbf6d4ef95efb3639a17bb7da05ee12d75f01cc05a62c9d309,',
    'HBB_HC': '7f192527065da0108ee062fb0aeaccf3319533fd5b9858633f6ac6a86ee88d5713486ba0ef97014be2f1fa3e8ccaa2c288',
    'HOY_TR': 'KBGJTOENFCMQWIRS,61A2345798BCDEF0,Etzrkosgxfhwbpuj,0',
    'Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd': '1748593331',
    'Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5': '1748593589',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&start_time=&end_time=&timeType=2&searchparam=&searchchannel=0&dbselect=bidx&kw=&bidSort=0&pinMu=0&bidType=0&buyerName=&projectId=&displayZone=&zoneId=&agentName=',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1748586074; HMACCOUNT=F4026F981A65044E; HMF_CI=be3cb6eb91ef0a81f68cc494e55a00b380880e2bf19923df62dca68c903a3537c81cbe8e72f564d5645ee6c1423c12cd8a574a71639096678700da37fd05b48840; Hm_lvt_9459d8c503dd3c37b526898ff5aacadd=1748586076; JSESSIONID=-RUgSMh2tKrnaAlZpvwftk5Oop59tX0g1Ng9nzkqbfBH9uySl8HS!485428781; HMY_JC=07fe7b45ebcd1eedcbf6d4ef95efb3639a17bb7da05ee12d75f01cc05a62c9d309,; HBB_HC=7f192527065da0108ee062fb0aeaccf3319533fd5b9858633f6ac6a86ee88d5713486ba0ef97014be2f1fa3e8ccaa2c288; HOY_TR=KBGJTOENFCMQWIRS,61A2345798BCDEF0,Etzrkosgxfhwbpuj,0; Hm_lpvt_9459d8c503dd3c37b526898ff5aacadd=1748593331; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1748593589',
}

params = {
    'searchtype': '1',
    'page_index': '1',
    'bidSort': '0',
    'buyerName': '',
    'projectId': '',
    'pinMu': '0',
    'bidType': '7',
    'dbselect': 'bidx',
    'kw': '',
    'start_time': '2025:05:23',
    'end_time': '2025:05:30',
    'timeType': '2',
    'displayZone': '',
    'zoneId': '',
    'pppStatus': '0',
    'agentName': '',
}

response = requests.get('https://search.ccgp.gov.cn/bxsearch', params=params, cookies=cookies, headers=headers).text

print(response)

html_content = response

pattern = r'var ohtmlurls="([^"]+)"'
match = re.search(pattern, html_content)

if match:
    ohtmlurls_value = match.group(1)
    print("ohtmlurls 的值为：")
    print(ohtmlurls_value)
else:
    print("未找到 ohtmlurls 的值")