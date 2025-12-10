from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import random
import os

# 创建Edge浏览器选项
edge_options = Options()

# 基础反检测设置
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_experimental_option("useAutomationExtension", False)

# 加载本地用户数据目录（保留你的设置）
user_data_dir = r"E:\edge_data\User Data"
edge_options.add_argument(f"--user-data-dir={user_data_dir}")

# Edge驱动路径（替换为你的实际路径）
driver_path = r"E:\edgedriver_win32\msedgedriver.exe"
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"Edge驱动不存在: {driver_path}")

# 初始化浏览器驱动
driver = webdriver.Edge(
    service=Service(driver_path),
    options=edge_options
)

# 注入真实浏览器指纹（核心步骤）
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        // 1. 模拟真实插件列表（与真实浏览器完全一致）
        class RealPlugin {
            constructor(name, description, filename, mimeTypes) {
                this.name = name;
                this.description = description;
                this.filename = filename;
                this.mimeTypes = mimeTypes;
            }
        }
        class RealPluginArray {
            constructor() {
                // 真实浏览器的5个PDF插件
                this.plugins = [
                    new RealPlugin(
                        "PDF Viewer",
                        "Portable Document Format",
                        "internal-pdf-viewer",
                        ["application/pdf", "text/pdf"]
                    ),
                    new RealPlugin(
                        "Chrome PDF Viewer",
                        "Portable Document Format",
                        "internal-pdf-viewer",
                        ["application/pdf", "text/pdf"]
                    ),
                    new RealPlugin(
                        "Chromium PDF Viewer",
                        "Portable Document Format",
                        "internal-pdf-viewer",
                        ["application/pdf", "text/pdf"]
                    ),
                    new RealPlugin(
                        "Microsoft Edge PDF Viewer",
                        "Portable Document Format",
                        "internal-pdf-viewer",
                        ["application/pdf", "text/pdf"]
                    ),
                    new RealPlugin(
                        "WebKit built-in PDF",
                        "Portable Document Format",
                        "internal-pdf-viewer",
                        ["application/pdf", "text/pdf"]
                    )
                ];
                this.length = this.plugins.length;
            }
            item(index) { return this.plugins[index] || null; }
            namedItem(name) { return this.plugins.find(p => p.name === name) || null; }
            [Symbol.iterator]() { return this.plugins[Symbol.iterator](); }
        }
        navigator.plugins = new RealPluginArray();

        // 2. 模拟真实MIME类型（与真实浏览器一致）
        class RealMimeTypeArray {
            constructor() {
                this.mimeTypes = [
                    { type: "application/pdf", suffixes: "pdf", description: "Portable Document Format" },
                    { type: "text/pdf", suffixes: "pdf", description: "Portable Document Format" }
                ];
                this.length = this.mimeTypes.length;
            }
            item(index) { return this.mimeTypes[index] || null; }
            namedItem(type) { return this.mimeTypes.find(m => m.type === type) || null; }
        }
        navigator.mimeTypes = new RealMimeTypeArray();

        // 3. 模拟真实语言设置（与真实浏览器一致）
        Object.defineProperty(navigator, 'languages', {
            get: () => ['zh-CN', 'en', 'en-GB', 'en-US']
        });

        // 4. 模拟navigator原型属性顺序（严格按照真实浏览器的顺序）
        const realNavigatorOrder = [
            "vendorSub", "productSub", "vendor", "maxTouchPoints", "scheduling", 
            "userActivation", "doNotTrack", "geolocation", "connection", "plugins", 
            "mimeTypes", "pdfViewerEnabled", "webkitTemporaryStorage", "webkitPersistentStorage",
            "windowControlsOverlay", "hardwareConcurrency", "cookieEnabled", "appCodeName",
            "appName", "appVersion", "platform", "product", "userAgent", "language",
            "languages", "onLine", "webdriver", "getGamepads", "javaEnabled", "sendBeacon",
            "vibrate", "constructor"
            // 省略部分属性，保持与真实浏览器顺序一致
        ];
        // 重排序navigator属性（核心伪装）
        const originalNavigator = { ...navigator };
        realNavigatorOrder.forEach(key => {
            if (originalNavigator.hasOwnProperty(key)) {
                Object.defineProperty(navigator, key, {
                    get: () => originalNavigator[key]
                });
            }
        });

        // 5. 隐藏WebDriver标识
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });

        // 6. 模拟真实videoCard（显卡信息）
        const originalGetParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {
            if (parameter === 37445) return "Google Inc. (Intel)"; // 供应商
            if (parameter === 37446) return "ANGLE (Intel, Intel(R) Iris(R) Xe Graphics (0x0000A7A0) Direct3D11 vs_5_0 ps_5_0, D3D11)"; // 渲染器
            return originalGetParameter.call(this, parameter);
        };

        // 7. 修复破损图片尺寸
        const style = document.createElement('style');
        style.textContent = `
            img:-webkit-broken {
                width: 200px !important;
                height: 200px !important;
                visibility: hidden;
            }
        `;
        document.head.appendChild(style);

        // 8. 模拟真实chrome对象（修复detailChrome错误）
        window.chrome = {
            runtime: { constructor: function() {} },
            webstore: { constructor: function() {} },
            app: { constructor: function() {} }
        };
    """
})

# 目标URL
target_url = 'https://fingerprintjs.github.io/BotD/main/'

# 'https://www.amia-crawler.com/'
# https://bot.sannysoft.com/

try:
    driver.get(target_url)
    print(f"已打开网站: {target_url}")

    input("请确认指纹匹配后按Enter键...")

except Exception as e:
    print(f"错误: {e}")
finally:
    input("按Enter键关闭浏览器...")
    driver.quit()