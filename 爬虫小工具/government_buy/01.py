import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://cn.bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    # 'cookie': 'qcc_did=29dc32b8-8667-43a9-95cc-88e2baec0723; UM_distinctid=1971bcbf016492-08a555738f860b8-4c657b58-168000-1971bcbf01720c5; tfstk=g0lqwLAIiId2l5EYnbNN4IoKzBNYn5-B_fZ_SV0gloqcGssiUVitGRxYGfor-D8T1SGX_APxNx1_cnFZSDNwAHOBOq3YB5xBAbM6c4VgSCZMF-4R3x2pAHOBNS_FabxIf1xMJUzTqr4gmlYzEyU_sGfiju2u-ys0scmgE74UuOb0SRflZuUgslmgsUuu2PPgjb74sWCz8-YtXGlyKZD03k0041uxar2VHqqPs1crU-rh_u5Gsbzq784kl6J_xvEbdknkNsPZrPozdx-FgcuiJA2r_iYjxVmxaSFeCEeEEYMQ3Y-c_uGb7JVgUNfizqqSYjVHtgz-EqMiMm7NsrhjORrLUFfTC7cQKvmVWe3uiPmTpftdMo0iJXHQTISLuY0UagolXz0ZpfHVjOy0yzrBzUowlZiUCXmIxOBTHaUzAELABOe0yzrBzUWOB-K8zkTvk; acw_tc=0a47318a17526314834576734e0062fdc9de86ba5830bf2636d64c05c1758c; QCCSESSID=2b6e899bc643808a28f65edd09; CNZZDATA1254842228=1427997727-1748518040-https%253A%252F%252Fcn.bing.com%252F%7C1752632242',
}

response = requests.get('https://www.qcc.com/firm/106acd2781b0e39042b17b55d2cd1aca.html', headers=headers)
print(response.text)