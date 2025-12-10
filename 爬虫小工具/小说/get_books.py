import requests

import re

from bs4 import BeautifulSoup

kv_dict = {
    "dushi":"1",
    "yanqing":"2",
    "tongren":"3",
    "xiuzhen":"4",
    "xuanhuan":"5",
    "wangyou":"6",
    "lishi":"7",
    "qita":"9",
    "kehuan":"10",
}

cookies = {
        'ngojmlastsearchtime': '1746084151',
        'sc_is_visitor_unique': 'rx12883304.1746084161.5A1A8611727E46929AF27F8E883EF5A0.1.1.1.1.1.1.1.1.1',
    }

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.baoshu7.com',
        'priority': 'u=0, i',
        'referer': 'https://www.baoshu7.com/',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    }

search_url = 'https://www.baoshu7.com/e/search/index.php'

base_url = 'https://www.baoshu7.com'

def tool(url,data=None):
    response = requests.post(url, cookies=cookies, headers=headers, data=data)
    return response.text


def get_book_name(keyboard):
    data = {
        'show': 'title,softsay,softwriter',
        'keyboard': keyboard,
        'Submit22': '',
        'tbname': 'download',
        'tempid': '1',
    }
    html = tool(search_url, data)
    soup = BeautifulSoup(html, 'html.parser')
    h4_tags = soup.find_all('h4')

    result = []
    for h4 in h4_tags:
        a_tag = h4.find('a')
        if a_tag:
            href = a_tag.get('href')
            title = a_tag.get('title')
            result.append({'href': href, 'title': title})
        else:
            return None
    return result

def get_down_url(groups):
    if groups:
        num = 1
        for book in groups:
            print(num, book['title'])
            num = num + 1
        index = int(input("请输入要下载内容的序号:"))
        if index > len(groups):
            return None
        temp_href = groups[index - 1]['href']
        pattern = r"/txt/([^/]+)/"
        match = re.search(pattern, temp_href)
        numbers = re.findall(r'\d+', temp_href)
        if numbers:
            num = ''.join(numbers)
        else:
            return None
        if match:
            result = match.group(1)
        else:
            return None
        return f"https://www.baoshu7.com/down/d{kv_dict[result]}t{num}baoshu.html"
    return None

def down_txt(url):
    # print(url)
    html = tool(url)
    soup = BeautifulSoup(html, 'html.parser')
    # 找到所有的 <li> 标签
    li_tags = soup.find_all('li')
    if li_tags:
        first_li = li_tags[0]  # 获取第一个 <li> 标签
        a_tag = first_li.find('a', href=True)  # 在第一个 <li> 标签中找 <a> 标签
        if a_tag:
            href = a_tag['href']
            # print(href)
            file_name = href[href.rfind('/') + 1:]
            # print(file_name)
            try:
                response = requests.get(href)
                response.raise_for_status()
                with open(file_name, 'w', encoding='ISO-8859-1') as file:
                    file.write(response.text)
                print("文件下载成功。")
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP 错误发生: {http_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"请求错误发生: {req_err}")
            except Exception as e:
                print(f"发生未知错误: {e}")


        else:
            print("在第一个 <li> 标签中未找到 <a> 标签。")
    else:
        print("未找到 <li> 标签。")


if __name__ == '__main__':
    search_keyboard = input('请输入书名(不要加书名号):')
    book_groups = get_book_name(search_keyboard)
    if book_groups:
        txt_url = get_down_url(book_groups)
        down_txt(txt_url)
    else:
        print("无搜索结果。")