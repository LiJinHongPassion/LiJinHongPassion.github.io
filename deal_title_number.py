import re
import os

def remove_title_numbers(file_path):
    # 读取Markdown文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 使用正则表达式匹配标题序号并去除
    content = re.sub(r'^\d+(\.\d+)?\. ', '', content, flags=re.MULTILINE)

    # 保存内容到原文件
    with open(file_path, 'w') as file:
        file.write(content)

def get_all_file_paths(directory_path):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
    return file_paths

def add_title_numbers(file_path):
    # 读取Markdown文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 逐级增加标题序号
    for level in range(1, 4):
        # 使用正则表达式匹配标题并添加序号
        pattern = r'(^|\n)#{' + str(level) + r'}\s+(.*?)$'
        replacement = '\\1#' + '.'.join(str(i) for i in range(1, level+1)) + ' \\2'
        content = re.sub(pattern, replacement, content)

    # 保存内容到原文件
    with open(file_path, 'w') as file:
        file.write(content)

def main(directory_path):
    file_list = get_all_file_paths(directory_path)
    for file_name in file_list:
        if file_name.endswith(".md") and '项目接入APIG网关' in file_name:
            print('处理标题', file_name)
            file_path = os.path.join(directory_path, file_name)
            remove_title_numbers(file_path)
            add_title_numbers(file_path)

# 获取当前执行文件的路径（绝对路径）
current_path = os.path.abspath(__file__)
print("当前执行文件的路径：", current_path)

# 获取当前执行文件所在目录的路径
current_directory = os.path.dirname(current_path)
main(current_directory)