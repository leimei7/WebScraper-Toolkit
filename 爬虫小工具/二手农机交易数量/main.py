import requests
import time
import random
import string

import hashlib

def md5_hash(input_string):
    # 将输入字符串编码为字节类型
    input_bytes = input_string.encode('utf-8')
    # 创建 MD5 哈希对象
    md5 = hashlib.md5()
    # 更新哈希对象的内容
    md5.update(input_bytes)
    # 获取十六进制表示的哈希值
    hash_hex = md5.hexdigest()
    return hash_hex

def random_string():
    source_str = string.ascii_letters + string.digits
    pwd = ''.join(random.choice(source_str) for _ in range(20))
    return pwd

cookies = {
    'ASP.NET_SessionId': 'k2fdww5wzqa5zcwdyvcon1sc',
    'Hm_lvt_df6121546e9c44610ea4ee9b7a11c93a': '1744589351',
    'HMACCOUNT': '4F01C978615D7DB2',
    'Hm_lpvt_df6121546e9c44610ea4ee9b7a11c93a': '1744589922',
}

def get_datas(page):
    data = {
        'keyword': '拖拉机',
        'lat': '0',
        'lng': '0',
        'p': page,
        'brand': '',
        'area': '',
        'pricearea': '0',
        'year': '0',
        'workhours': '0',
        'source': '-1',
        'category': '0',
        'onlyguzi': '1',
        'mftid': '',
    }
    i1 = 'sowebsite'
    i2 = '20220222'
    r1 = i1 + i2
    i3 = int(time.time())
    r2 = r1 + str(i3)
    i4 = str(random_string())
    r3 = r2 + i4
    i5 = 'ahfBynI7PTCXv_VGai38aZ0zUSA6T'
    sign = md5_hash(r3 + i5)

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'apiappid': i1,
        'apiverb': i2,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'nonce': i4,
        'origin': 'https://so.nongjitong.com',
        'priority': 'u=1, i',
        'referer': 'https://so.nongjitong.com/SecondHand/mobileSearch.html',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'signature': sign,
        'timestamp': str(i3),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'ASP.NET_SessionId=k2fdww5wzqa5zcwdyvcon1sc; Hm_lvt_df6121546e9c44610ea4ee9b7a11c93a=1744589351; HMACCOUNT=4F01C978615D7DB2; Hm_lpvt_df6121546e9c44610ea4ee9b7a11c93a=1744589922',
    }

    response = requests.post('https://so.nongjitong.com/API/GetList.ashx', cookies=cookies, headers=headers, data=data)
    return response.json()


if __name__ == '__main__':
    total_count = 0
    for i in range(1, 51):
        datas = get_datas(i)

        print(datas)

        with open('output.csv', 'a', encoding='utf-8') as file:  # 使用 'a' 模式追加写入，避免每次循环覆盖
            count = 0
            print("page:",count)
            for item in datas["data"]:
                title = item["Title"]
                price = item["Price"]
                province = item["Province"]
                line = f"Title: {title}, Price: {price}, Province: {province}\n"
                file.write(line)
                count += 1
                print("写入:",count)
            total_count += count
    print(f"总共写入了 {total_count} 条数据到 output.csv 文件中。")