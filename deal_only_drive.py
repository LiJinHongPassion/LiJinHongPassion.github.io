import os

def filter_md_files(folder_path):
    # 遍历文件夹
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                # 读取文件内容
                with open(file_path, 'r') as file:
                    content = file.read()
                # 判断是否包含"onlyOneDrive: true"
                if "onlyOneDrive: true" in content or "onlyOneDrive: \"true\"" in content or "onlyOneDrive: \"True\"" in content or "onlyOneDrive: \"TRUE\"" in content:
                    # 遍历.gitignore文件
                    gitignore_path = os.path.join(folder_path, '.gitignore')
                    # 读取.gitignore文件内容
                    with open(gitignore_path, 'r') as gitignore_file:
                        gitignore_content = gitignore_file.read()
                    # 判断是否已经存在相同内容
                    add_ignore_file_path = os.path.relpath(file_path, folder_path)
                    if add_ignore_file_path in gitignore_content:
                        continue
                    # 添加内容到.gitignore文件末尾
                    with open(gitignore_path, 'a') as gitignore_file:
                        gitignore_file.write("\n" + add_ignore_file_path + " # onlyOneDrive \n")
                        print('add_ignore_file_path', add_ignore_file_path)
# 获取当前执行文件的路径（绝对路径）
current_path = os.path.abspath(__file__)
print("当前执行文件的路径：", current_path)

# 获取当前执行文件所在目录的路径
current_directory = os.path.dirname(current_path)
# 使用示例
filter_md_files(current_directory)