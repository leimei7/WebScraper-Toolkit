import asyncio
import random
import time
import atexit
import csv  # 引入csv模块处理CSV文件
from pyppeteer import launch
from pyppeteer.browser import Browser
import requests

# 全局浏览器实例，避免频繁创建和关闭
browser: Browser | None = None

async def init_browser(user_data_dir: str):
    """初始化浏览器实例"""
    global browser
    if not browser:
        browser = await launch(
            headless=False,
            executablePath=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            userDataDir=user_data_dir,
            args=[
                "--no-sandbox",
                "--disable-gpu",
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
            ],
            ignoreDefaultArgs=["--enable-automation"],
            slowMo=10,
        )
        # 注册程序退出时的清理函数（优化事件循环处理）
        atexit.register(lambda: asyncio.get_event_loop().run_until_complete(
            close_browser()) if asyncio.get_event_loop().is_running() else None)
    return browser


async def close_browser():
    """关闭浏览器实例"""
    global browser
    if browser:
        await browser.close()
        browser = None


async def fetch_zp_stoken(user_data_dir: str) -> str | None:
    """从BOSS直聘网站获取__zp_stoken__ cookie值"""
    browser = await init_browser(user_data_dir)
    page = await browser.newPage()

    try:
        await page.setViewport({"width": 1536, "height": 912, "deviceScaleFactor": 1.0})

        # 注入反检测脚本
        await page.evaluateOnNewDocument("""
            () => {
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                Object.defineProperty(navigator, 'languages', { get: () => ['zh-CN', 'zh', 'en-US', 'en'] });
                delete window.__pyppeteer;
            }
        """)

        # 访问BOSS直聘并等待页面加载完成
        await page.goto("https://www.zhipin.com/", waitUntil="networkidle2")
        await asyncio.sleep(random.uniform(5, 7))

        # 获取所有cookie并筛选__zp_stoken__
        cookies = await page.cookies()
        zp_stoken = next((cookie for cookie in cookies if cookie['name'] == '__zp_stoken__'), None)
        return zp_stoken['value'] if zp_stoken else None

    finally:
        await page.close()


def get_request(query, pages, zp_token):
    """发送请求获取职位列表数据"""
    cookies = {
        '__zp_stoken__': zp_token,
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
        response = requests.get(
            'https://www.zhipin.com/wapi/zpgeek/search/joblist.json',
            params=params,
            cookies=cookies,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if data['code'] != 0:
            print(f"请求异常 code: {data['code']}")
            return None
        return data
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


def code():
    while True:
        code_id = input("请输入项目编号: ").strip()
        if code_id:
            return code_id
        else:
            print("项目编号不能为空，请重新输入！")


def get_token_count():
    """获取用户输入的token数量（正整数）"""
    while True:
        try:
            count = int(input("请输入需要获取的token数量: ").strip())
            if count > 0:
                return count
            else:
                print("token数量必须为正整数，请重新输入！")
        except ValueError:
            print("输入无效，请输入一个整数！")


def get_datas(json_data, writer):
    """解析并保存职位数据（包含encryptJobId），返回是否有有效数据"""
    if not json_data or "zpData" not in json_data or "jobList" not in json_data["zpData"]:
        print("未获取到有效职位数据结构")
        return False

    job_contents = json_data["zpData"]["jobList"]
    if not job_contents:  # 核心判断：职位列表为空
        print("当前页无职位数据，停止爬取")
        return False

    for idx, job_content in enumerate(job_contents, 1):
        try:
            # 提取职位唯一标识（新增字段）
            encrypt_job_id = job_content.get('encryptJobId', '未知')

            # 提取其他职位数据
            jobName = job_content.get('jobName', '未知')
            salaryDesc = job_content.get('salaryDesc', '未标注')
            skills = job_content.get('skills', '无')
            jobDegree = job_content.get('jobDegree', '不限')
            jobExperience = job_content.get('jobExperience', '无要求')
            brandName = job_content.get('brandName', '未标注公司')
            cityName = job_content.get('cityName', '全国')
            bossName = job_content.get('bossName', '未显示')
            welfareList = ', '.join(job_content.get('welfareList', [])) or '无福利'

            # 生成职位链接
            securityId = job_content.get('securityId', '')
            url = f"https://www.zhipin.com/job_detail/{encrypt_job_id}.html?securityId={securityId}" if encrypt_job_id != '未知' and securityId else "链接生成失败"

            # 写入CSV（包含encryptJobId）
            writer.writerow([
                encrypt_job_id,  # 职位唯一标识（新增）
                jobName,
                salaryDesc,
                skills,
                jobDegree,
                jobExperience,
                brandName,
                cityName,
                bossName,
                welfareList,
                url
            ])
        except Exception as e:
            print(f"解析第{idx}条数据时出错: {e}")

    return True  # 有有效数据则返回True


async def main():
    user_data_dir = r"E:\edge_data\User Data"
    query_keyword = query()
    code_id = code()
    token_count = get_token_count()
    pages_per_token = 5
    total_pages = token_count * pages_per_token

    count = 0
    filename = f"{code_id}_{query_keyword}_职位信息.csv"

    try:
        with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            # 写入表头（新增encryptJobId列）
            writer.writerow([
                "encryptJobId",  # 新增表头
                "职位名称",
                "薪资",
                "技能要求",
                "学历要求",
                "工作经验",
                "公司名称",
                "城市",
                "招聘负责人",
                "福利",
                "职位链接"
            ])

            for token_idx in range(token_count):
                print(f"\n===== 获取第{token_idx + 1}/{token_count}个token =====")

                zp_token = await fetch_zp_stoken(user_data_dir)
                if not zp_token:
                    print("未能获取到有效的token，跳过当前批次")
                    continue

                print(f"成功获取token: {zp_token[:20]}...")

                start_page = token_idx * pages_per_token + 1
                end_page = min((token_idx + 1) * pages_per_token, total_pages)

                for page in range(start_page, end_page + 1):
                    print(f"\n正在爬取第{page}页数据...")
                    json_data = get_request(query_keyword, page, zp_token)

                    wait_time = random.uniform(2, 5)
                    print(f"等待{wait_time:.1f}秒后继续...")
                    await asyncio.sleep(wait_time)

                    if json_data:
                        has_data = get_datas(json_data, writer)
                        if not has_data:
                            print("检测到无数据，终止爬取流程")
                            await close_browser()
                            print(f"\n数据已成功保存至: {filename}")
                            print(f"共爬取{count * 30}条职位信息（实际有效数据以文件内容为准）")
                            return
                        count += 1
                    else:
                        print(f"第{page}页数据获取失败，尝试下一页...")

    except Exception as e:
        print(f"程序运行出错: {e}")
    finally:
        await close_browser()  # 确保浏览器关闭

    print(f"\n数据已成功保存至: {filename}")
    print(f"共爬取{count * 30}条职位信息（实际有效数据以文件内容为准）")


if __name__ == "__main__":
    # 适配Windows系统事件循环
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())