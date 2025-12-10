from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import random
import string

# 配置Edge浏览器
driver_path = r"E:\edgedriver_win32\msedgedriver.exe"  # Edge驱动路径
user_data_dir = r"E:\edge_data\User Data"  # Edge用户数据目录

# 常用User-Agent列表
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
]


def random_sleep(min_sec=1, max_sec=3):
    """随机等待一段时间，模拟人类行为"""
    wait_time = random.uniform(min_sec, max_sec)
    print(f"等待 {wait_time:.2f} 秒")
    time.sleep(wait_time)


def random_string(length=10):
    """生成随机字符串"""
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def scroll_to_bottom(driver, scroll_pause_time=1):
    """
    滚动页面到底部，触发所有内容加载

    参数:
    driver: WebDriver实例
    scroll_pause_time: 每次滚动后的暂停时间（秒）
    """
    # 获取初始页面高度
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 随机滚动到页面不同位置
        scroll_position = random.randint(70, 90) / 100
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {scroll_position});")

        # 随机等待
        random_sleep(0.5, 1.5)

        # 滚动到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 等待页面加载
        random_sleep(scroll_pause_time - 0.3, scroll_pause_time + 0.3)

        # 获取新的页面高度
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 如果高度没有变化，说明已经到底部
        if new_height == last_height:
            # 再尝试一次，确保没有延迟加载的内容
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            random_sleep(scroll_pause_time - 0.3, scroll_pause_time + 0.3)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

        last_height = new_height
        print(f"已滚动，页面高度: {last_height}")


def get_rendered_html(url, timeout=10):
    """获取指定URL渲染后的HTML内容，增加反爬策略"""
    # 创建Edge浏览器选项
    edge_options = Options()
    edge_options.add_argument(f"--user-data-dir={user_data_dir}")

    # 随机窗口大小，模拟不同设备
    width = random.randint(1200, 1920)
    height = random.randint(768, 1080)
    edge_options.add_argument(f"--window-size={width},{height}")

    # 随机User-Agent
    user_agent = random.choice(USER_AGENTS)
    edge_options.add_argument(f"--user-agent={user_agent}")
    print(f"使用User-Agent: {user_agent}")

    # 禁用WebDriver特征
    edge_options.add_argument("--disable-blink-features=AutomationControlled")

    # 创建Edge浏览器实例
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        # 设置随机超时
        driver.set_page_load_timeout(random.randint(30, 60))

        print(f"正在打开页面: {url}")
        driver.get(url)

        # 等待页面加载完成
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        # 随机等待，模拟人类浏览行为
        random_sleep(2, 5)

        print("页面加载完成，开始滚动以触发所有内容加载...")

        # 滚动页面到底部多次，确保所有内容加载完成
        scroll_to_bottom(driver)

        # 随机等待，模拟阅读行为
        random_sleep(3, 7)

        # 获取渲染后的HTML内容
        html_content = driver.page_source
        print(f"成功获取页面内容，长度: {len(html_content)} 字符")

        return html_content

    except Exception as e:
        print(f"获取页面内容时出错: {e}")
        return None

    finally:
        # 关闭浏览器
        input("按回车键退出浏览器...")
        driver.quit()


if __name__ == "__main__":
    # 指定要获取的URL
    target_url = "https://www.zhipin.com/web/geek/jobs?query=%E8%85%BE%E8%AE%AF&city=100010000"

    # 获取渲染后的HTML
    rendered_html = get_rendered_html(target_url, timeout=15)

    if rendered_html:
        # 打印HTML内容的前1000个字符
        print("\nHTML内容预览:")
        print(rendered_html[:1000])

        # 保存完整内容到文件
        with open("rendered_page.html", "w", encoding="utf-8") as file:
            file.write(rendered_html)
        print("\n完整内容已保存到 rendered_page.html")