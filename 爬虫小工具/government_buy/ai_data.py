import requests
import json
import mysql.connector
from mysql.connector import Error

# DeepSeek API配置
API_KEY = "sk-d2443da053e5498aa87e1744aaf624c8"  # 替换为你的API密钥
API_URL = "https://api.deepseek.com/v1/chat/completions"  # 根据实际文档调整

# 请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 数据库配置 - 根据你的MySQL设置修改
DB_CONFIG = {
    'host': 'localhost',
    'database': 'gbdb',
    'user': 'root',
    'password': '*****',
    'charset': 'utf8mb4',
    'autocommit': True
}


def generate_text(prompt: str, model: str = "deepseek-chat") -> str:
    """
    调用DeepSeek API生成文本

    Args:
        prompt: 用户输入的提示文本
        model: 要使用的模型名称

    Returns:
        生成的文本内容
    """
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,  # 控制随机性，范围0-2，默认0.7
        "max_tokens": 2000  # 最大生成长度
    }

    try:
        # 发送请求
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))

        # 检查响应状态
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None

    except Exception as e:
        print(f"发生异常: {e}")
        return None


def create_table():
    """创建存储JSON数据的表"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            create_table_query = """
                                 CREATE TABLE IF NOT EXISTS procurement_data \
                                 ( \
                                     id \
                                     INT \
                                     AUTO_INCREMENT \
                                     PRIMARY \
                                     KEY, \
                                     project_code \
                                     VARCHAR \
                                 ( \
                                     255 \
                                 ),
                                     project_name VARCHAR \
                                 ( \
                                     255 \
                                 ),
                                     json_data JSON
                                     ) \
                                 """
            cursor.execute(create_table_query)
            print("表创建成功或已存在")
    except Error as e:
        print(f"创建表时出错: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def insert_data(json_array):
    """将JSON数组中的数据插入数据库"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            insert_query = """
                           INSERT INTO procurement_data (project_code, project_name, json_data)
                           VALUES (%s, %s, %s) \
                           """

            for item in json_array:
                project_code = item.get("项目编号", "None")
                project_name = item.get("项目名称", "None")
                json_data = json.dumps(item, ensure_ascii=False)

                cursor.execute(insert_query, (project_code, project_name, json_data))

            print(f"成功插入 {cursor.rowcount} 条记录")

    except Error as e:
        print(f"插入数据时出错: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# 使用示例
if __name__ == "__main__":
    prompt = input("输入:")
    text = """将上面每一条数据变为一个json数组，注意如果同一个项目编号下面有多个中标供应商，只保留首条记录，保证同一个项目编号只要一条记录，其中每一条结构如{
            "项目编号": "",
            "项目名称": "",
            "采购单位": "",
            "中标供应商": {
            "名称": "",（如果出现同一个项目编号下面有多个中标供应商，填入"多"，读者自然就知道原本有多条记录）
            "地址": "",
            "中标金额": "",
            "评审得分": ""
            },
            "公告时间": ""
            }
            没有的填入null，格式如下
            {
        """
    generated_text = generate_text(prompt + text)

    if generated_text:
        # 去除字符串中的```json和```标记（如果存在）
        cleaned_text = generated_text.strip('`json\n').rstrip('`')

        try:
            # 解析JSON字符串为Python列表
            data_array = json.loads(cleaned_text)

            print(data_array)

        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            print(f"解析的文本: {cleaned_text}")