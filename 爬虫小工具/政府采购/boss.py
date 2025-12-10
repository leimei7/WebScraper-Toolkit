import requests

def get_request(query, index):
    """发送请求获取JSON数据"""
    cookies = {
        'lastCity': '101281000',
        '__g': 'sem_bingpc',
        'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1733815947',
        'HMACCOUNT': 'C4603FF5FD89DD5B',
        'wt2': 'DQ2hpC-SxREB8wHy5UR_O4qaluW35qPJ9KVXv5QgM8eGApk5z0ypsu98w0SL25-oEvW5LpyAhS4PycAKyuPooYw~~',
        'wbg': '0',
        'zp_at': 'LyeHbf68ytEAiQMeRW6-LCn4NJwmyMxsRCsDEqZKm8Q~',
        'ab_guid': '2b362c14-998a-440d-bb02-05eef4dd9395',
        '__zp_seo_uuid__': '49f53280-4c27-4cbf-95ec-0408792918f9',
        '__l': 'r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fjob_detail%2Fd26a271e94045f4a1nZ73d-6EldR.html%3FsecurityId%3DuLxGTJgMPVWS1-e1rsVGxSKsL3FywIfBX8gEylrv1njeOrszuB8J7ffbmTYVN4BmMLnaoCQ~%26sessionId%3D&s=3&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3F_ts%3D1733819062714%26sid%3Dsem_bingpc%26qudao%3Dbing_pc_H120003UY5%26plan%3DBOSS-%25E5%25BF%2585%25E5%25BA%2594-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2594-%25E7%25AC%25A6%25E5%258F%25B7%25E8%25AF%258D%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2594%25E7%25BD%2591%25E9%25A1%25B5%25E7%2589%2588%2528%26msclkid%3D7be2972fe9d11696e67af0781364e48b&friend_source=0&s=3&friend_source=0',
        'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1733830631',
        '__zp_stoken__': '63fafOTzDmsK4w4LCujksBQYIDQ5DKjY8Mx9COTA7Nz45PD01PDk8NRc6KSXCvMOVwoJuWsOSNTUkPD1ANTk6PTdAFDw5xLnCujg9JsOZwrXDm3tqYcOKW8KCDsKBK8OkwrwOScK1CsO1w4IrJ8KBwr1COEI2Y8K%2FOMOABsK%2BQsOCCsK7Q8K4ODo2Qyg0ElsKDzQ6RVJfCkhhU1VgTARKS1EoNjg8N8OdwrjEgyY1CgYTEggTDwoLEQUJDAgSEAwJCBITDwoLES05wpnDgsOIxoDFgMKLxJnFqsOTwrHEoMKMxJbEgsOMwovEvsKWxLHDtMOXwrzDoMKPw5rCpsOjwrjDvFLDskbEuMKsw79KwonCp8OJwq3EgsKSw4pIw5%2FCtsOywqrClGLChMKfw63CtcSCWcO5UMKOwq7CpU7DgVjCiFLCpl7CtsK8wrnCqE1QwrBMw4HCt8KUwrRhwrlJclzCg8Ktwrd8dXh3w4JVcmdcY14NCz5UDXjDiQ%3D%3D',
        'bst': 'V2R98gEOP43VtiVtRuzBkQKSy27DrSwi8~|R98gEOP43VtiVtRuzBkQKSy27DrRxC8~',
        '__c': '1733815946',
        '__a': '51952642.1728739453.1728742713.1733815946.53.3.48.48',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': 'https://www.zhipin.com/web/geek/job?query=%E7%88%AC%E8%99%AB',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': 'yPy6F3g6gvwbyWll',
        'traceid': 'F-dccebbJEbotxD75U',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        'zp_token': 'V2R98gEOP43VtiVtRuzBkQKSy27DrSwi8~|R98gEOP43VtiVtRuzBkQKSy27DrRxC8~',
    }

    params = {
        'scene': '1',
        'query': query,
        'city': '',  # 空字符串表示全国范围
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
        'page': index,
        'pageSize': '30',
    }

    try:
        response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', 
                                params=params, cookies=cookies, headers=headers, timeout=10)
        response.raise_for_status()  # 抛出HTTP错误
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None

def user_input_query():
    """获取用户输入的职位关键词"""
    while True:
        query = input("请输入职位关键词（如'Python开发'）: ").strip()
        if query:
            return query
        else:
            print("关键词不能为空，请重新输入！")

def get_data(json_data, f):
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
    query = user_input_query()
    
    # 生成文件名并打开文件（UTF-8编码避免中文乱码）
    filename = f"全国_{query}_职位信息.csv"
    try:
        with open(filename, 'w', encoding='utf-8-sig') as f:  # utf-8-sig带BOM兼容Excel
            # 写入CSV表头
            f.write("职位名称,薪资,技能要求,学历要求,工作经验,公司名称,城市,招聘负责人,福利,职位链接\n")
            
            # 爬取前4页数据（可根据需要调整页数范围）
            for page in range(1, 5):
                print(f"正在爬取第{page}页数据...")
                json_data = get_request(query, page)
                if json_data:
                    get_data(json_data, f)
                else:
                    print(f"第{page}页数据获取失败，跳过...")
    
    except Exception as e:
        print(f"文件操作出错: {e}")
    else:
        print(f"\n数据已成功保存至: {filename}")
        print(f"共爬取{page * 30}条职位信息（实际有效数据以文件内容为准）")