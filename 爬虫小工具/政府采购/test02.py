import requests

cookies = {
    'wt2': 'DQL1kXWgv15okm8Q4lG02ZJ6ibdMAxnbjnOcFQOhlp6pPOCJ1hcHhZaxIZhKQFR3zOSgweZsMtejNeztxZr9HwA~~',
    'wbg': '0',
    'zp_at': 'xO2z9T1hAgyCJuyjTZAHTLoo6Z-4TDvcW-A0bQB1Ofo~',
    'ab_guid': 'c456c365-067c-45e5-b9c0-cac931b30e81',
    '__g': 'sem_bingpc',
    'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1748586537,1748594915',
    'HMACCOUNT': 'F4026F981A65044E',
    '__zp_seo_uuid__': '6e55d07a-614a-4ab0-b392-5588d9301b6a',
    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1748595899',
    'bst': 'V2R9ohF-T_0lxjVtRuyxQbKym47DrXxSo~|R9ohF-T_0lxjVtRuyxQbKym47Drfxyo~',
    '__c': '1748594914',
    '__l': 'r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjobs%3Fquery%3D%25E8%25BE%25BD%25E5%25AE%2581%25E6%25B5%25A9%25E4%25BA%25BF&s=3&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1748595893289%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3Dbeb7f5619ce1197a2e299d58e84e17a1&friend_source=0&s=3&friend_source=0',
    '__a': '36300358.1748586537.1748586533.1748594914.26.2.23.23',
    '__zp_stoken__': '4157fQTfDocOAwp3Dgko6BwQMBBpLLTY3LRpCQTM1N0FBN0s1Q0E3Qxc9MXvDi8ObUhlow4xPSiQ3S0hKQUlLNzcUNzfFgcK9QDYwH8OKw41PE2jDjRJtaXQZZQRbBFDDgT05w6HDijZANEDDvcODQMK2wrDDiDbDisKswrU9wrxAPEA9LDRqaxIZNDxTTGMSTl9NaWhSEkRPWS5ANkA3ZMObw706NRoGGxAGGAQZEgQHGwYQBgwQDQYQGwcaEQczN8KpwrbErcWkxI3CssScxbLDhcKvxJ7Dp8OfwprDjMOvw5XClcWBw7bDqcOJw6TCtsSwwqfEtMK9xILCnMS0wrjDmk3DvsK6wpLCjsO5wpnEiMKNw6rCtMOdw4vCok3CksOCwqDCucOxwrrCsmjDi0TCq8KuwpZOwrXDgsKiUsKSZcOCU8KMXcKyw4rCvmhcwrBFcsK7w4DCrWLCuXLDiFvCgFPDgmpgXQ%2FCgWANEQUHQlRlw5TDhg%3D%3D',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'priority': 'u=1, i',
    'referer': 'https://www.zhipin.com/web/geek/jobs?city=101271000&query=%E8%BE%BD%E5%AE%81%E6%B5%A9%E4%BA%BF',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': 'OPGHy8UQ0vyHOTPi',
    'traceid': 'F-847ac40Wzz475sRz',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'zp_token': 'V2R9ohF-T_0lxjVtRuyxQbKym47DrXxSo~|R9ohF-T_0lxjVtRuyxQbKym47Drfxyo~',
    # 'cookie': 'wt2=DQL1kXWgv15okm8Q4lG02ZJ6ibdMAxnbjnOcFQOhlp6pPOCJ1hcHhZaxIZhKQFR3zOSgweZsMtejNeztxZr9HwA~~; wbg=0; zp_at=xO2z9T1hAgyCJuyjTZAHTLoo6Z-4TDvcW-A0bQB1Ofo~; ab_guid=c456c365-067c-45e5-b9c0-cac931b30e81; __g=sem_bingpc; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1748586537,1748594915; HMACCOUNT=F4026F981A65044E; __zp_seo_uuid__=6e55d07a-614a-4ab0-b392-5588d9301b6a; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1748595899; bst=V2R9ohF-T_0lxjVtRuyxQbKym47DrXxSo~|R9ohF-T_0lxjVtRuyxQbKym47Drfxyo~; __c=1748594914; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjobs%3Fquery%3D%25E8%25BE%25BD%25E5%25AE%2581%25E6%25B5%25A9%25E4%25BA%25BF&s=3&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1748595893289%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3Dbeb7f5619ce1197a2e299d58e84e17a1&friend_source=0&s=3&friend_source=0; __a=36300358.1748586537.1748586533.1748594914.26.2.23.23; __zp_stoken__=4157fQTfDocOAwp3Dgko6BwQMBBpLLTY3LRpCQTM1N0FBN0s1Q0E3Qxc9MXvDi8ObUhlow4xPSiQ3S0hKQUlLNzcUNzfFgcK9QDYwH8OKw41PE2jDjRJtaXQZZQRbBFDDgT05w6HDijZANEDDvcODQMK2wrDDiDbDisKswrU9wrxAPEA9LDRqaxIZNDxTTGMSTl9NaWhSEkRPWS5ANkA3ZMObw706NRoGGxAGGAQZEgQHGwYQBgwQDQYQGwcaEQczN8KpwrbErcWkxI3CssScxbLDhcKvxJ7Dp8OfwprDjMOvw5XClcWBw7bDqcOJw6TCtsSwwqfEtMK9xILCnMS0wrjDmk3DvsK6wpLCjsO5wpnEiMKNw6rCtMOdw4vCok3CksOCwqDCucOxwrrCsmjDi0TCq8KuwpZOwrXDgsKiUsKSZcOCU8KMXcKyw4rCvmhcwrBFcsK7w4DCrWLCuXLDiFvCgFPDgmpgXQ%2FCgWANEQUHQlRlw5TDhg%3D%3D',
}

params = {
    'page': '1',
    'pageSize': '15',
    'query': '辽宁浩亿',
    'city': '101271000',
    'expectInfo': '',
    'multiSubway': '',
    'multiBusinessDistrict': '',
    'position': '',
    'jobType': '',
    'salary': '',
    'experience': '',
    'degree': '',
    'industry': '',
    'scale': '',
    'stage': '',
    'scene': '1',
    '_': '1748597242564',
}

response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', params=params, cookies=cookies, headers=headers)

print(response.text)