import asyncio
import random
from pyppeteer import launch


async def get_zp_stoken(user_data_dir):
    # 启动浏览器
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

    page = await browser.newPage()
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
    await page.goto("https://www.zhipin.com/", waitUntil="networkidle2")  # 等待网络稳定
    await asyncio.sleep(random.uniform(5, 6))  # 随机等待，模拟用户浏览

    # 获取所有cookie并筛选__zp_stoken__
    cookies = await page.cookies()
    zp_stoken = next((cookie for cookie in cookies if cookie['name'] == '__zp_stoken__'), None)

    # 输出结果
    if zp_stoken:
        print(f"获取到__zp_stoken__: {zp_stoken['value']}")
    else:
        print("未获取到__zp_stoken__（可能需要登录或页面未完全加载）")

    # 关闭浏览器
    await browser.close()
    return zp_stoken


async def main():
    user_data_dir = r"E:\edge_data\User Data"
    loop_count = 5  # 循环次数

    for i in range(loop_count):
        print(f"\n===== 第{i + 1}/{loop_count}次循环 =====")

        # 执行获取操作
        await get_zp_stoken(user_data_dir)

        # 循环间隔（最后一次不需要间隔）
        if i < loop_count - 1:
            wait_time = random.uniform(50, 60)  # 随机间隔8-15秒
            print(f"等待{wait_time:.1f}秒后进行下一次...")
            await asyncio.sleep(wait_time)

    print("\n所有循环执行完毕")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())