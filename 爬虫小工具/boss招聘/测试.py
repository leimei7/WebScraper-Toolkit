from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import re


def get_zp_stoken(driver):
    # 执行JavaScript获取cookie
    cookies = driver.execute_script("return document.cookie")
    match = re.search(r'__zp_stoken__=([^;]+)', cookies)
    if match:
        token = match.group(1)
        print(f"[{time.strftime('%H:%M:%S')}] __zp_stoken__: {token}")
        return token
    else:
        print(f"[{time.strftime('%H:%M:%S')}] 未找到__zp_stoken__")
        return None


def main():
    # 配置Chrome选项
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # 取消注释可无头运行

    # 初始化驱动
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # 打开BOSS直聘
        driver.get("https://www.zhipin.com")
        print("已打开BOSS直聘，等待页面加载...")
        time.sleep(10)  # 等待页面加载（可根据网络调整）

        # 循环执行（模拟手动刷新）
        for i in range(5):  # 执行5次，可改为while True无限循环
            # 获取Token
            token = get_zp_stoken(driver)

            # 随机等待10-15秒
            wait_time = random.randint(10, 15)
            print(f"[{time.strftime('%H:%M:%S')}] 等待{wait_time}秒后刷新...")
            time.sleep(wait_time)

            # 刷新页面
            driver.refresh()
            print(f"[{time.strftime('%H:%M:%S')}] 已刷新页面")
            time.sleep(5)  # 等待刷新后加载

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        input("按Enter键退出...")
        driver.quit()


if __name__ == "__main__":
    main()