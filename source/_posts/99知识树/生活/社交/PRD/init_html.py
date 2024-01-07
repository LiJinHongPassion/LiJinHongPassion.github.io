import os
import json

source_file = os.path.abspath(__file__)
source_dir = os.path.dirname(source_file)
# 读取HTML文件内容
with open(source_dir + '/show-person-relation-diagram.html', 'r', encoding='utf8') as f:
    content = f.readlines()

# 删除insert-start和insert-end之间的行
for index, line in enumerate(content): 
    if 'insert-start' in line:
        start = index
    if 'insert-end' in line:
        end = index
del content[start+1:end]

# 写入HTML文件
with open(source_dir + '/show-person-relation-diagram.html', 'w',encoding='utf8') as f:
    f.writelines(content)

# 读取JSON文件内容
with open(source_dir + '/data.json', 'r',encoding='utf8') as f:
    data = json.load(f)

# 将users和relations字段的值转换为字符串
users_str = 'var nodes = ' + json.dumps(data['users']) + '\n'
relations_str = 'var edges = ' + json.dumps(data['relations']) + '\n'

# 找到insert-start和insert-end之间的行
for index, line in enumerate(content): 
    if 'insert-start' in line:
        start = index + 1
    if 'insert-end' in line:
        end = index

# 将users和relations字段的值插入到insert-start和insert-end之间的行
content.insert(start, users_str)
content.insert(start, relations_str)

# 写入HTML文件
with open(source_dir + '/show-person-relation-diagram.html', 'w',encoding='utf8') as f:
    f.writelines(content)
