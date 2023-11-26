import re
import os

# 格式化标题
# 标题格式只能为 # 1. 标题

def remove_title_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.startswith("#") and '# ' in line:
            group = line.split(" ")
            if len(group) == 3 and group[1].endswith('.'):
                # 去除序号部分
                new_line = group[0] + " " + group[2]
            else:
               new_line = line 
        else:
            new_line = line
        
        new_lines.append(new_line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def get_all_file_paths(directory_path):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
    return file_paths

def add_title_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    new_lines = []
    title_count = [0, 0, 0]  # 用于记录每个级别标题的序号

    for line in lines:
        if line.startswith("#") and '# ' in line and '.' not in line:
            group = line.split(' ')
            num = ''
            if len(group) == 2 and len(group[0]) < 4:
                if group[0] == '#':
                    title_count[0] += 1
                    num = str(title_count[0])
                    title_count[1] = 0
                    title_count[2] = 0
                elif group[0] == '##':
                    title_count[1] += 1
                    num = str(title_count[0]) + '.' + str(title_count[1])
                    title_count[2] = 0
                elif group[0] == '###':
                    title_count[2] += 1
                    num = str(title_count[0]) + '.' + str(title_count[1]) + '.' + str(title_count[2])
                new_line = group[0] + ' ' + num + ". " + group[1]
            else: 
                new_line = line 
        else:
            new_line = line
        
        new_lines.append(new_line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)
   
def main(directory_path):
    file_list = get_all_file_paths(directory_path)
    for file_name in file_list:
        if file_name.endswith(".md"):
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