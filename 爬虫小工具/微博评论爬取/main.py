import requests
from jsonpath_ng import parse
import re
from bs4 import BeautifulSoup
import time

#通用连接
def tool(param,url):
    cookies = {
        'SCF': 'Ak_F1md8swjlu0KYSzXGEz8T-XoYtCDKgNVFcZYPH_4CdujE1wB3wrIMudVcnGlkfjwIf2NLUz7RWxcbG3CMtZs.',
        'SUB': '_2A25K56PqDeRhGeRN7lsV8CfOyT-IHXVpnLkirDV8PUNbmtANLWX3kW1NU5oWYp_o-bZzm1GmRdi7Vg-0zgStbPl5',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5cAFPF7I9ycqGHaF43lzVC5NHD95QEe0-4Sh54eoz0Ws4DqcjVi--ciKn4iKyFi--ciKLhi-iWi--NiK.Xi-2Ri--ciKnRi-zNeoef1KB71KzEe7tt',
        'ALF': '02_1745576122',
        'WBPSESS': 'DXTJO8iWaF0oaqHHfCvBjG0XGGnupv2KzeslBXc00IESQHsjaCg0dQFe8YwjPECytS3kJOCANfRfB5hMXCifGlqLa0_fgvINCiajEY6bbZKNPlqinObvq5UNQvE4vBvX-QYeaRBYWnXjtXTJSdSHRw==',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'client-version': 'v2.47.43',
        # 'cookie': 'SCF=Ak_F1md8swjlu0KYSzXGEz8T-XoYtCDKgNVFcZYPH_4CdujE1wB3wrIMudVcnGlkfjwIf2NLUz7RWxcbG3CMtZs.; SUB=_2A25K56PqDeRhGeRN7lsV8CfOyT-IHXVpnLkirDV8PUNbmtANLWX3kW1NU5oWYp_o-bZzm1GmRdi7Vg-0zgStbPl5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5cAFPF7I9ycqGHaF43lzVC5NHD95QEe0-4Sh54eoz0Ws4DqcjVi--ciKn4iKyFi--ciKLhi-iWi--NiK.Xi-2Ri--ciKnRi-zNeoef1KB71KzEe7tt; ALF=02_1745576122; WBPSESS=DXTJO8iWaF0oaqHHfCvBjG0XGGnupv2KzeslBXc00IESQHsjaCg0dQFe8YwjPECytS3kJOCANfRfB5hMXCifGlqLa0_fgvINCiajEY6bbZKNPlqinObvq5UNQvE4vBvX-QYeaRBYWnXjtXTJSdSHRw==',
        'priority': 'u=1, i',
        'referer': 'https://weibo.com/2015316631/NeHdrwNAF',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'server-version': 'v2025.03.24.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    response = requests.get(url, params=param, cookies=cookies,
                            headers=headers)
    return response

#去除<>元素
def replace_img_tags(data):
    for item in data:
        if item.get('text'):
            item['text'] = re.sub(r'<[^>]*>', '表情', item['text'])
    return data

#获取帖子
def get_topics(page):
    param = {
        'q': '阳江鱼',
        'page': page,
    }

    html = tool(param,'https://s.weibo.com/weibo').text

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', attrs={'class': 'card-wrap', 'action-type': 'feed_list_item'})
    mid_s = [div['mid'] for div in divs if 'mid' in div.attrs]

    result_dict = {f'mid{iq + 1}': mid_q for iq, mid_q in enumerate(mid_s)}

    return result_dict

#获得客服需要的信息
def get_all(m_id):
    params = {
        'is_reload': '1',
        'id': m_id,
        'is_show_bulletin': '2',
        'is_mix': '0',
        'count': '10',
        'uid': '2015316631',
        'fetch_level': '0',
        'locale': 'zh-CN',
    }
    json_data = tool(params,'https://weibo.com/ajax/statuses/buildComments').json()
    expressions = {
        'created_at': parse('$.data[*].created_at'),
        'text': parse('$.data[*].text'),
        'source': parse('$.data[*].source'),
        'user_id': parse('$.data[*].user.id'),
        'screen_name': parse('$.data[*].user.screen_name')
    }
    result = []
    num_items = len(expressions['created_at'].find(json_data))

    for ii in range(num_items):
        item = {}
        for key, expr in expressions.items():
            matches = expr.find(json_data)
            if key == 'user_id':
                item["sex"] = get_sex(matches[ii].value)
                time.sleep(0.5)
            item[key] = matches[ii].value if ii < len(matches) else None
        result.append(item)
    return replace_img_tags(result)

#为了获得性别
def get_sex(u_id):
    params = {
        'uid': u_id,
        'containerid': f'100505{u_id}',
    }
    data = tool(params,'https://m.weibo.cn/api/container/getIndex').json()

    jsonpath_expr = parse('$.data.userInfo.gender')
    results = jsonpath_expr.find(data)

    if results:  # 检查列表是否为空
        return results[0].value
    return None


if __name__ == '__main__':
    try:
        with open('yj.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            count = len(lines)
    except FileNotFoundError:
        count = 0

    with open('yj.txt', 'a', encoding='utf-8') as file:
        for i in range(1, 50):

            if count == 500:
                break

            print("page:", i)
            mid_dict = get_topics(i)
            for mid in mid_dict.values():
                alls = get_all(mid)
                if len(alls) == 0:
                    continue
                for al in alls:
                    # 将字典的值转换为字符串，用空格连接
                    values_str = " ".join(str(value) for value in al.values())
                    # 写入文件
                    file.write(values_str + '\n')
                    count += 1
                    print(f"已写入 {count} 条记录")
                time.sleep(0.2)