import pandas as pd


def extract_info(line):
    # 按固定长度提取时间
    time = line[:24]

    # 提取评论
    from_index = line.find(" 来自")
    comment = line[24:from_index].strip()

    # 提取地方、性别和名字
    remaining_text = line[from_index + 3:].strip()

    # 查找性别位置
    gender_index_male = remaining_text.find("男")
    gender_index_female = remaining_text.find("女")
    if gender_index_male != -1:
        gender_index = gender_index_male
        gender = "男"
    elif gender_index_female != -1:
        gender_index = gender_index_female
        gender = "女"
    else:
        gender_index = -1
        gender = None

    # 提取地方
    if gender_index != -1:
        place = remaining_text[:gender_index].strip()
    else:
        place = remaining_text

    # 提取名字
    if gender_index != -1:
        name_start = gender_index + 1
        while name_start < len(remaining_text) and remaining_text[name_start].isspace():
            name_start += 1
        name = remaining_text[name_start:] if name_start < len(remaining_text) else None
    else:
        name = None

    return time, comment, place, gender, name


file_path = 'atm.txt'  # 替换为实际的文件路径
data = []
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            time, comment, place, gender, name = extract_info(line)
            data.append([time, comment, place, gender, name])

    df = pd.DataFrame(data, columns=['时间', '评论', '地方', '性别', '名字'])
    output_file = 'output.xlsx'
    df.to_excel(output_file, index=False)
    print(f"数据已成功保存到 {output_file}")
except FileNotFoundError:
    print(f"错误：未找到文件 {file_path}。")
except Exception as e:
    print(f"发生未知错误：{e}")
    