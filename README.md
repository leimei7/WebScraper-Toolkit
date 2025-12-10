# 爬虫小工具集合

这是一个包含多个爬虫小项目的集合，用于演示不同网站的爬取技术和实现方式。每个项目都有其特定的功能和用途，下面将详细介绍每个项目的功能、使用方法和依赖项。

## 目录结构

```
爬虫小工具/
├── QQ音乐登录/          # QQ音乐登录系统
├── boss招聘/             # Boss直聘职位信息爬虫
├── government_buy/       # 政府采购中标公告爬虫
├── hand-spider/          # 手动选择图片下载爬虫
├── 二手农机交易数量/       # 二手农机交易数量爬虫
├── 小说/                 # 小说下载爬虫
├── 微博评论爬取/          # 微博评论爬取系统
└── 政府采购/             # 政府采购信息爬虫
```

## 项目介绍

### 1. QQ音乐登录

**功能说明**：使用Flask搭建的QQ音乐登录系统，通过二维码登录获取QQ音乐的登录凭证（m_key）。

**实现技术**：
- Flask框架搭建Web服务
- Requests库处理HTTP请求
- 二维码生成和扫描验证
- 多线程处理登录状态检查

**使用方法**：
1. 安装依赖：`pip install flask flask-cors requests`
2. 运行主程序：`python flask测试.py`
3. 访问API获取登录二维码：`http://localhost:5000/newlogin/qrcode/`
4. 扫描二维码登录
5. 检查登录状态：`http://localhost:5000/newlogin/check_status/`

### 2. Boss招聘

**功能说明**：Boss直聘网站的职位信息爬虫，支持获取职位详情和公司信息。

**实现技术**：
- Requests库处理HTTP请求
- Pyppeteer进行动态页面渲染
- 反混淆JavaScript代码
- 自动化采集Cookies

**主要文件**：
- `get_all.py`：获取职位信息的主程序
- `get_cookies.py`：获取登录Cookies
- `deobfuscator.py`：JavaScript反混淆工具
- `pyppeteer/`：使用Pyppeteer的动态爬虫脚本

### 3. government_buy

**功能说明**：政府采购网站中标公告爬虫，用于提取中标公告的关键信息。

**实现技术**：
- BeautifulSoup进行HTML解析
- 结构化数据提取
- 日志记录

**主要文件**：
- `buy_datas.py`：提取公告内容的核心功能
- `buy_urls.py`：获取公告URL列表
- `ai_data.py`：AI辅助数据处理

**使用方法**：
```python
from buy_datas import extract_content

# 传入HTML内容，返回提取的结构化数据
data = extract_content(html_content)
```

### 4. hand-spider

**功能说明**：手动选择的图片下载爬虫，可以根据需要下载指定的图片。

**实现技术**：
- Requests库处理HTTP请求
- 命令行交互

**主要文件**：
- `get_imgs.py`：图片下载主程序
- `hand_choose.py`：手动选择功能
- `color.py`：颜色处理工具

### 5. 二手农机交易数量

**功能说明**：爬取二手农机交易数量的爬虫，用于统计和分析农机交易数据。

**实现技术**：
- 结合JavaScript和Python的混合爬虫
- 动态数据获取

**主要文件**：
- `main.py`：主程序入口
- `1.js`：辅助JavaScript脚本
- `test.py`：测试脚本

### 6. 小说

**功能说明**：小说下载爬虫，支持根据关键词搜索小说并下载TXT格式。

**实现技术**：
- Requests库处理HTTP请求
- BeautifulSoup解析HTML
- 正则表达式提取信息

**使用方法**：
```python
from get_books import get_book_name, get_down_url, down_txt

# 搜索小说
books = get_book_name("关键词")
# 获取下载链接
down_url = get_down_url(books)
# 下载小说
down_txt(down_url)
```

**运行示例**：
```
python get_books.py
请输入书名(不要加书名号): 三体
1 三体全集
2 三体Ⅰ：地球往事
3 三体Ⅱ：黑暗森林
4 三体Ⅲ：死神永生
请输入要下载内容的序号: 1
文件下载成功。
```

### 7. 微博评论爬取

**功能说明**：爬取微博评论的爬虫，支持根据关键词搜索帖子并获取评论信息，包括评论内容、发布时间、用户信息等。

**实现技术**：
- Requests库处理HTTP请求
- BeautifulSoup解析HTML
- JsonPath提取JSON数据
- 正则表达式处理文本

**主要功能**：
- 根据关键词搜索微博帖子
- 获取帖子的评论列表
- 提取评论用户的性别信息
- 评论内容清洗和处理

**使用方法**：
```python
from main import get_topics, get_all

# 获取帖子ID列表
topics = get_topics(1)  # 第1页
# 获取评论信息
for mid in topics.values():
    comments = get_all(mid)
    print(comments)
```

**配置说明**：
- 修改`main.py`中的cookies配置为有效的微博登录cookies
- 修改搜索关键词：`get_topics`函数中的`q`参数

### 8. 政府采购

**功能说明**：政府采购信息爬虫，用于获取政府采购的职位信息和详情。

**主要文件**：
- `boss.py`：主程序入口
- `page.py`：分页处理
- `detail.py`：详情页处理
- `test01.py`、`test02.py`：测试脚本

## 技术栈

| 技术/库 | 用途 | 项目使用情况 |
|---------|------|--------------|
| Python | 主要开发语言 | 所有项目 |
| Requests | HTTP请求处理 | 所有项目 |
| BeautifulSoup | HTML解析 | 大部分项目 |
| Flask | Web服务搭建 | QQ音乐登录 |
| Pyppeteer | 动态页面渲染 | Boss招聘 |
| JsonPath | JSON数据提取 | 微博评论爬取 |
| re | 正则表达式处理 | 多个项目 |
| Threading | 多线程处理 | QQ音乐登录 |

## 环境要求

- Python 3.7+ 
- 各项目所需的第三方库（见每个项目的具体依赖）

## 安装依赖

建议使用虚拟环境安装各项目的依赖：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
env\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt  # 部分项目提供了requirements.txt
# 或根据每个项目的需求单独安装
pip install flask requests beautifulsoup4 jsonpath-ng
```

## 使用注意事项

1. **遵守网站规则**：使用爬虫时请遵守目标网站的 robots.txt 规则和使用条款，不要过度请求导致服务器压力。

2. **Cookies 配置**：部分项目需要配置有效的登录Cookies才能正常运行，请根据实际情况更新Cookies。

3. **请求频率控制**：建议在爬取过程中添加适当的延迟，避免被网站封禁IP。

4. **动态页面处理**：对于使用JavaScript动态加载的内容，需要使用Pyppeteer或Selenium等工具进行处理。

5. **反爬策略**：部分网站可能有反爬机制，需要根据实际情况调整爬取策略，如更换User-Agent、使用代理IP等。

## 项目扩展建议

1. **添加数据库存储**：将爬取的数据存储到数据库中，方便后续查询和分析。

2. **增加GUI界面**：为部分项目添加图形用户界面，提高易用性。

3. **实现分布式爬取**：对于大规模数据爬取，考虑使用分布式架构提高爬取效率。

4. **添加数据可视化**：对爬取的数据进行可视化处理，生成图表或报告。

5. **完善错误处理**：增加更健壮的错误处理机制，提高爬虫的稳定性。

## 许可证

本项目仅供学习和研究使用，不得用于商业用途。使用本项目造成的任何后果由使用者自行承担。

## 贡献

欢迎提交Issue和Pull Request，共同完善这个爬虫工具集合。
---

**免责声明**：本项目仅用于学习和研究目的，请勿用于任何非法用途。使用本项目造成的一切后果由使用者自行承担。
