import time
import random

import requests

# 先刷新页面多获得几个__zp_stoken__，存放在这里面
# 可以使用selenium自动刷新再采集
zp = ''

# name = 'd9aec51e'
# seed = 'LKEGh/SyKqBL4pNDX0IsLWTCGnCBNDPjP6X+ikxlaNk='
# t = '1749185995141'
"""
zp = r = (new e).z(t, parseInt(n) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3)
t = cookie.__zp_sseed__
parseInt(n) = cookie.__zp_sts__ // str
parseInt(n) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3 = cookie.__zp_sts__ // int
(new e).z(cookie.__zp_sseed__,cookie.__zp_sts__)
(new e).z关键加密
"""

def get_request(query,pages):
    cookies = {
        '__zp_stoken__': zp,
        'lastCity': '101270100',
        'wt2': 'D6HghwDCepwtedsR71CAuyyJPsrxHqw3hqVSqmIDmkosW4nklhQd_gnUsX8UEHkpWQvMpoT0FjuEIzI78orxKnQ~~',
        'wbg': '0',
        'zp_at': 'ICPOhzfjwRylSD1AXpZr0QRv9UHkYuEPKauHOGs7co8~',
        '__zp_seo_uuid__': '50edf72e-90f5-44c9-ab65-08697565b2ab',
        '__g': 'sem_bingpc',
        '__l': 'r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1750917231726%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3D24999f57ac6619c5979df70b4c0b6d1a&s=1&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1750917231726%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E7%25B2%25BE%25E5%2587%2586%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%26msclkid%3D24999f57ac6619c5979df70b4c0b6d1a&s=3&friend_source=0',
        'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1750914744,1750915900,1750916385,1750917235',
        'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1750917235',
        'HMACCOUNT': 'EE2C631D6CC05F87',
        '__c': '1750917232',
        '__a': '12364210.1750905430.1750916382.1750917232.49.9.3.3',
        'BAIDUID_BFESS': '75C89348E095F1A1D125748402ED2BC4:FG=1',
        'ab_guid': 'd3643ee8-a80c-4da2-965d-16b8726f16cf',
        'bst': 'V2R9ohF-T_0lxjVtRuyhwfLSmw7DrSwys~|R9ohF-T_0lxjVtRuyhwfLSmw7DrezCU~',
   }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'priority': 'u=1, i',
        'referer': 'https://www.zhipin.com/web/geek/jobs?query=%E8%85%BE%E8%AE%AF&city=101270100',
        'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': 'ihzWemCouhxcuJCs',
        'traceid': 'F-1ac6f1sOQjMGwE05',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        'zp_token': 'V2R9ohF-T_0lxjVtRuyhwfLSmw7DrSwys~|R9ohF-T_0lxjVtRuyhwfLSmw7DrezCU~',
   }

    params = {
        'scene': '1',
        'query': query,
        'city': '',  # 全国范围
        'experience': '',
        'payType': '',
        'partTime': '',
        'degree': '',
        'industry': '',
        'scale': '',
        'stage': '',
        'position': '',
        'jobType': '',
        'salary': '',
        'multiBusinessDistrict': '',
        'multiSubway': '',
        'page': pages,
        'pageSize': '30',
    }

    try:
        response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json',
                                params=params, cookies=cookies, headers=headers, timeout=10)
        response.raise_for_status()  # 抛出HTTP错误
        data = response.json()
        if data['code'] != 0:
            print("cookies有误 code:",data['code'])
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None

def query():
    """获取用户输入的职位关键词"""
    while True:
        query = input("请输入职位关键词（如'Python开发'）: ").strip()
        if query:
            return query
        else:
            print("关键词不能为空，请重新输入！")

def get_datas(json_data, f):
    """解析并保存职位数据"""
    if not json_data or "zpData" not in json_data or "jobList" not in json_data["zpData"]:
        print("未获取到有效职位数据")
        return

    job_contents = json_data["zpData"]["jobList"]
    for idx, job_content in enumerate(job_contents, 1):
        try:
            jobName = job_content.get('jobName', '未知')
            salaryDesc = job_content.get('salaryDesc', '未标注')
            skills = job_content.get('skills', '无')
            jobDegree = job_content.get('jobDegree', '不限')
            jobExperience = job_content.get('jobExperience', '无要求')
            brandName = job_content.get('brandName', '未标注公司')
            cityName = job_content.get('cityName', '全国')
            bossName = job_content.get('bossName', '未显示')
            welfareList = ', '.join(job_content.get('welfareList', [])) or '无福利'  # 处理福利列表

            # 构建职位链接（注意部分字段可能为空）
            encryptJobId = job_content.get('encryptJobId', '')
            securityId = job_content.get('securityId', '')
            if encryptJobId and securityId:
                url = f"https://www.zhipin.com/job_detail/{encryptJobId}.html?securityId={securityId}"
            else:
                url = "链接生成失败"

            # 写入CSV文件（逗号分隔，含中文需确保编码正确）
            f.write(f"{jobName},{salaryDesc},{skills},{jobDegree},{jobExperience},{brandName},{cityName},{bossName},{welfareList},{url}\n")
        except Exception as e:
            print(f"解析第{idx}条数据时出错: {e}")

if __name__ == '__main__':
    # 获取用户输入的职位关键词
    query = query()

    count = 0

    # UTF-8编码
    filename = f"全国_{query}_职位信息.csv"
    try:
        with open(filename, 'w', encoding='utf-8-sig') as f:  # utf-8-sig带BOM兼容Excel
            # 写入CSV表头
            f.write("职位名称,薪资,技能要求,学历要求,工作经验,公司名称,城市,招聘负责人,福利,职位链接\n")

            #每5页必需换 zp_stoken
            for page in range(1, 6):
                print(f"正在爬取第{page}页数据...")
                json_data = get_request(query, page)
                time.sleep(random.randint(1, 3))
                if json_data:
                    get_datas(json_data, f)
                    count += 1
                else:
                    print(f"第{page}页数据获取失败，跳过...")

    except Exception as e:
        print(f"文件操作出错: {e}")
    else:
        print(f"\n数据已成功保存至: {filename}")
        print(f"共爬取{count * 30}条职位信息（实际有效数据以文件内容为准）")