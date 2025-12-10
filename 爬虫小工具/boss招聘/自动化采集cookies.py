from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import random
import os

# 配置Edge浏览器选项（核心：加载本地用户数据目录）
edge_options = Options()
edge_options.add_argument("--start-maximized")  # 最大化窗口，模拟真实使用
edge_options.add_argument("--disable-blink-features=AutomationControlled")  # 反检测核心参数
edge_options.add_argument("--excludeSwitches=enable-automation")  # 隐藏自动化开关
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 隐藏自动化开关
edge_options.add_experimental_option("useAutomationExtension", False)  # 禁用自动化扩展

# 关键：加载本地Edge用户数据目录（替换为你的实际路径）
# 路径格式：C:\Users\你的用户名\AppData\Local\Microsoft\Edge\User Data
user_data_dir = r"E:\edge_data\User Data"
edge_options.add_argument(f"--user-data-dir={user_data_dir}")

# 可选：指定特定配置文件（如果有多个用户，默认是Default）
# edge_options.add_argument("--profile-directory=Default")

# Edge驱动路径（替换为你的实际路径）
driver_path = r"E:\edgedriver_win32\msedgedriver.exe"

# 验证驱动文件是否存在
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"Edge驱动不存在: {driver_path}")

# 初始化浏览器驱动
driver = webdriver.Edge(
    service=Service(driver_path),
    options=edge_options
)

# 目标URL（直接访问，利用本地登录状态）
target_url = "https://www.zhipin.com"

try:
    # 打开目标网站（利用本地用户数据中的登录状态）
    driver.get(target_url)
    print(f"已打开网站: {target_url}")
    time.sleep(random.uniform(3, 5))  # 随机等待，模拟用户加载等待

    # 等待用户确认页面状态（确保已登录）
    input("请确认页面已正常登录，按Enter键开始获取__zp_stoken__...")

    # 设置循环次数
    refresh_count = 5

    # 存储所有__zp_stoken__的值
    zp_stokens = []

    for i in range(refresh_count):
        # 刷新页面
        driver.refresh()
        print(f"\n=== 第 {i + 1}/{refresh_count} 次刷新页面，等待5秒页面稳定...")
        time.sleep(5)  # 等待页面加载稳定

        # 获取当前所有Cookie
        cookies = driver.get_cookies()

        # 查找__zp_stoken__
        zp_stoken = None
        for cookie in cookies:
            if cookie['name'] == '__zp_stoken__':
                zp_stoken = cookie['value']
                break

        # 存储并打印结果
        if zp_stoken:
            zp_stokens.append(zp_stoken)
            print(f"=== 第 {i + 1}/{refresh_count} 次刷新后 __zp_stoken__: {zp_stoken}")
        else:
            zp_stokens.append("未找到__zp_stoken__")
            print(f"=== 第 {i + 1}/{refresh_count} 次刷新后 未找到__zp_stoken__")

        # 随机等待一段时间，模拟用户操作间隔
        random_wait = random.uniform(45, 60)
        print(f"随机等待 {random_wait:.2f} 秒...")
        time.sleep(random_wait)

        # 模拟用户滚动页面（更真实的行为）
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * Math.random());")  # 随机滚动位置
        time.sleep(random.uniform(1, 2))

    # 按指定格式输出所有__zp_stoken__
    print("\n\n最终结果（按指定格式输出）:")
    for i, token in enumerate(zp_stokens):
        print(f"'{token}',")

except Exception as e:
    print(f"发生错误: {e}")
finally:
    # 等待用户确认后关闭浏览器
    input("按Enter键关闭浏览器...")
    driver.quit()