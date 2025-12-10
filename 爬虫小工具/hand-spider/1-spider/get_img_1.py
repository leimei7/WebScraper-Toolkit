import requests

import time

cookies = {
    'sajssdk_2015_cross_new_user': '1',
    '_gid': 'GA1.2.66424947.1743481879',
    'queryKey': 'KEH2R4NQEN8',
    'st': 'VEER-ST-1698363-483-2ba4a151462a4d7b85b42d524f5a683e',
    'uid': '1698363',
    '_c_WBKFRo': 'AcwHZ4gWLZXTI32YxFx7t5cdaEzrkHR4PxZuUSVA',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.veer.com%2Fsearch-image%2Fshouzhijia%2F%3Fpage%3D3%22%7D%2C%22%24device_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%7D',
    'acw_tc': '1a0c638c17435070294436442e008d922a59f8043278c82260c7a740c14df7',
    'acw_sc__v2': '67ebce5547ef111767bf5259983ae7dfc867764c',
    'Hm_lvt_2663761a9226999365054376b04969e1': '1743490783,1743493343,1743505162,1743507031',
    'HMACCOUNT': '4F01C978615D7DB2',
    '_gat_gtag_UA_103598720_1': '1',
    'Hm_lpvt_2663761a9226999365054376b04969e1': '1743507066',
    '_ga_2TQ4PLYBNK': 'GS1.1.1743507031.5.1.1743507065.26.0.0',
    '_ga': 'GA1.2.1788631146.1743481879',
    '_fp_': 'eyJpcCI6IjIxOC4yMDAuMjI1LjE4MSIsImZwIjoiNTQzMDFlMzFkM2QyNWFhNTc0YTljMjYyNjcwNzA1MDgiLCJocyI6IiQyYSQwOCRxL0FNaEJ0T1FCZWhwTDRKdDBPSlkuT0hTZEZWdHJTeEoubkkvd01FOVI5cWZqQlRwbDltMiJ9',
    'vtoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdCI6IlZFRVItU1QtMTY5ODM2My00ODMtMmJhNGExNTE0NjJhNGQ3Yjg1YjQyZDUyNGY1YTY4M2UiLCJ0aWNrZXQiOiI2QjdFOERFMzNDNkYzMEI4NDFFN0U5NjEwMTI0ODBDNDg3RkZENTU1QkVBMEJGRjQyNjVBNEVFQjc1NTIwRDg1RDQ5Qjk0MzI2ODg5Q0ZGOTYzQTI5RTNCNzI3RUFCODciLCJwYXlTdGF0dXMiOiIiLCJ1aWQiOjE2OTgzNjMsIm5hbWUiOiLotKbmiLciLCJtb2JpbGUiOiIxODMqKioqNjM4NCIsInJlZ1RpbWUiOiIyMDI1LTA0LTAxIDE1OjAzOjU3IiwiYWNjb3VudEVtYWlsIjoiIiwiYWNjb3VudE1vYmlsZSI6IjE4MzgyMDc2Mzg0IiwiY29tcGFueU5hbWUiOiIiLCJjb21wYW55TmF0dXJlIjoiIiwidmNnSWQiOiI5NDI1MzA2YWM0YmEzODAxYTU0ZTk3NTI5NTVmZDM3OTMiLCJhdXRvTG9naW4iOjEsImlhdCI6MTc0MzUwNzA2NSwiZXhwIjo0MzM1NTA3MDY1fQ.xEbBfG-2o__4bT_1JPGcjOAmHPvqWmv1Wr7CYdteFas',
    'ssxmod_itna': 'mq+xRD9D0Dciq4BpxB++8+e0=D8Du0AjEG0lcxGwKhexDseQrDSxGKidDqxBWeU3PTW7ieqKXeZruoeXGAY9vxEzp3nLNtrjfTeDHxY=DUZoTLYD4+5GwD0eG+DD4DWDmn7DnxAQDjxGPg0wX/AqDEDYPxxiU0D7UqaeDj9Tt9FeG0DDtk4qG2CjtPDDNPQahn9Y=PWeD+4k2ZlQXN8pD4mqDMCeGX7GHPmTuzVahDk69krlP9DB6IxBj/feNNEAUxZq2oSBPqlbYqFxo4/GGWKAqPnRL57AYN/YmYWveq/YPPWHwYeRsDG+D3GDri4siDD=',
    'ssxmod_itna2': 'mq+xRD9D0Dciq4BpxB++8+e0=D8Du0AjEG0lcxGwKx4ikU1e1Dlp+4j+2F3U5q6tBDnR5Csiem7XNsAOGYxP519kYvwcezPxa8qT=Y34AsYlO0H4N0pflIXy8NZwhX=2hiC1c11CnUhS8IUBLY18YLM0O6RWBdhYiUIAO3oMRDqf2AtSD3rAhx1DgA5NAWXWofEiYP8YGxrPmoGmo3qecGuD8Y=P6w=DjN4nrWu/beCe+b0RTBzgCOvU37=o90Ot+h4qWnOAwGXGSjw4V0GOFYwqm7I4e3UHehL1RMrez=1YElvnx=XIRKiHB7pHYF/t9G3TB4KSCb/RKsiicUI1tiN8xSj7/QGOeKNWFOjTvYbYeIjeb3CpGY+2f2htn5znimpUe9WKb3=PWAwP64gBwan7VU+0QbQ5orK80AE0eTtPKWtWKEhrI+xW03oEWCGi905Gua0cfDHC0gK9TGjcaWGYPyNpnu+LGfBH73i6qtVWb33kXorSG4YIvfPwQ4stad05Wne/tC1hcrCyLATNMvrbxCndTIK23b86dGsj8lQqCBHzSlmdrQDTQvWx1s=44zoNsIymMrHykXpCO8lSd2AZL02WWx2dS261dCpaVdL/GdD07OIQW95kMYz73asw7XikvrDr3sHMxU=X+7k0nQRTPD5tBhnoQKUw5e4ExhnVQ9X=kDDLxD+ZYK0Djx9hx3DD',
    '_ga_S8P7R6WH5V': 'GS1.1.1743507031.5.0.1743507076.0.0.0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.veer.com',
    'Referer': 'https://www.veer.com/search-image/shouzhijia/?page=7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'sajssdk_2015_cross_new_user=1; _gid=GA1.2.66424947.1743481879; queryKey=KEH2R4NQEN8; st=VEER-ST-1698363-483-2ba4a151462a4d7b85b42d524f5a683e; uid=1698363; _c_WBKFRo=AcwHZ4gWLZXTI32YxFx7t5cdaEzrkHR4PxZuUSVA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.veer.com%2Fsearch-image%2Fshouzhijia%2F%3Fpage%3D3%22%7D%2C%22%24device_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%7D; acw_tc=1a0c638c17435070294436442e008d922a59f8043278c82260c7a740c14df7; acw_sc__v2=67ebce5547ef111767bf5259983ae7dfc867764c; Hm_lvt_2663761a9226999365054376b04969e1=1743490783,1743493343,1743505162,1743507031; HMACCOUNT=4F01C978615D7DB2; _gat_gtag_UA_103598720_1=1; Hm_lpvt_2663761a9226999365054376b04969e1=1743507066; _ga_2TQ4PLYBNK=GS1.1.1743507031.5.1.1743507065.26.0.0; _ga=GA1.2.1788631146.1743481879; _fp_=eyJpcCI6IjIxOC4yMDAuMjI1LjE4MSIsImZwIjoiNTQzMDFlMzFkM2QyNWFhNTc0YTljMjYyNjcwNzA1MDgiLCJocyI6IiQyYSQwOCRxL0FNaEJ0T1FCZWhwTDRKdDBPSlkuT0hTZEZWdHJTeEoubkkvd01FOVI5cWZqQlRwbDltMiJ9; vtoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdCI6IlZFRVItU1QtMTY5ODM2My00ODMtMmJhNGExNTE0NjJhNGQ3Yjg1YjQyZDUyNGY1YTY4M2UiLCJ0aWNrZXQiOiI2QjdFOERFMzNDNkYzMEI4NDFFN0U5NjEwMTI0ODBDNDg3RkZENTU1QkVBMEJGRjQyNjVBNEVFQjc1NTIwRDg1RDQ5Qjk0MzI2ODg5Q0ZGOTYzQTI5RTNCNzI3RUFCODciLCJwYXlTdGF0dXMiOiIiLCJ1aWQiOjE2OTgzNjMsIm5hbWUiOiLotKbmiLciLCJtb2JpbGUiOiIxODMqKioqNjM4NCIsInJlZ1RpbWUiOiIyMDI1LTA0LTAxIDE1OjAzOjU3IiwiYWNjb3VudEVtYWlsIjoiIiwiYWNjb3VudE1vYmlsZSI6IjE4MzgyMDc2Mzg0IiwiY29tcGFueU5hbWUiOiIiLCJjb21wYW55TmF0dXJlIjoiIiwidmNnSWQiOiI5NDI1MzA2YWM0YmEzODAxYTU0ZTk3NTI5NTVmZDM3OTMiLCJhdXRvTG9naW4iOjEsImlhdCI6MTc0MzUwNzA2NSwiZXhwIjo0MzM1NTA3MDY1fQ.xEbBfG-2o__4bT_1JPGcjOAmHPvqWmv1Wr7CYdteFas; ssxmod_itna=mq+xRD9D0Dciq4BpxB++8+e0=D8Du0AjEG0lcxGwKhexDseQrDSxGKidDqxBWeU3PTW7ieqKXeZruoeXGAY9vxEzp3nLNtrjfTeDHxY=DUZoTLYD4+5GwD0eG+DD4DWDmn7DnxAQDjxGPg0wX/AqDEDYPxxiU0D7UqaeDj9Tt9FeG0DDtk4qG2CjtPDDNPQahn9Y=PWeD+4k2ZlQXN8pD4mqDMCeGX7GHPmTuzVahDk69krlP9DB6IxBj/feNNEAUxZq2oSBPqlbYqFxo4/GGWKAqPnRL57AYN/YmYWveq/YPPWHwYeRsDG+D3GDri4siDD=; ssxmod_itna2=mq+xRD9D0Dciq4BpxB++8+e0=D8Du0AjEG0lcxGwKx4ikU1e1Dlp+4j+2F3U5q6tBDnR5Csiem7XNsAOGYxP519kYvwcezPxa8qT=Y34AsYlO0H4N0pflIXy8NZwhX=2hiC1c11CnUhS8IUBLY18YLM0O6RWBdhYiUIAO3oMRDqf2AtSD3rAhx1DgA5NAWXWofEiYP8YGxrPmoGmo3qecGuD8Y=P6w=DjN4nrWu/beCe+b0RTBzgCOvU37=o90Ot+h4qWnOAwGXGSjw4V0GOFYwqm7I4e3UHehL1RMrez=1YElvnx=XIRKiHB7pHYF/t9G3TB4KSCb/RKsiicUI1tiN8xSj7/QGOeKNWFOjTvYbYeIjeb3CpGY+2f2htn5znimpUe9WKb3=PWAwP64gBwan7VU+0QbQ5orK80AE0eTtPKWtWKEhrI+xW03oEWCGi905Gua0cfDHC0gK9TGjcaWGYPyNpnu+LGfBH73i6qtVWb33kXorSG4YIvfPwQ4stad05Wne/tC1hcrCyLATNMvrbxCndTIK23b86dGsj8lQqCBHzSlmdrQDTQvWx1s=44zoNsIymMrHykXpCO8lSd2AZL02WWx2dS261dCpaVdL/GdD07OIQW95kMYz73asw7XikvrDr3sHMxU=X+7k0nQRTPD5tBhnoQKUw5e4ExhnVQ9X=kDDLxD+ZYK0Djx9hx3DD; _ga_S8P7R6WH5V=GS1.1.1743507031.5.0.1743507076.0.0.0',
}

def get_id(head,cookie,page):
    json_data = {
        'page': page,
        'urlPhrase': 'shouzhijia',
        'phrase': '手指甲',
        'graphicalStyle': '',
        'perpage': 100,
        'key': 'KEH2R4NQEN8',
        'page_type': 6,
        'isGraphicalStyleChange': False,
        'isPhraseChange': False,
        'anonyUid': 'FN6B13C01ID9',
        'favorid': '',
    }

    response = requests.post('https://www.veer.com/ajax/search', cookies=cookie, headers=head, json=json_data)
    print(response.text)
    return response.json()

def get_img(re_id):
    return f'https://veer01.cfp.cn/creative/vcg/veer/612/veer-{re_id}.jpg?x-oss-process=image/format,webp'

if __name__ == "__main__":
    total_count = 0
    with open('output1.txt', 'w', encoding='utf-8') as file:
        for i in range(1200,2500):
            data = get_id(headers, cookies, i)
            res_list = data.get('data', {}).get('list', [])
            res_ids = [item.get('resId') for item in res_list]
            if total_count == 100000:
                break
            for res_id in res_ids:
                result = get_img(res_id)
                file.write(str(result) + '\n')
                total_count += 1
                print(f"总共写入了 {total_count} 条内容到 output1.txt 文件中。")
            time.sleep(0.5)