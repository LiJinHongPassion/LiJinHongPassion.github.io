import os
import base64

def get_all_file_paths(directory_path):
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)
    return file_paths
def get_paths_with_suffix(paths, suffix):
    matching_paths = [path for path in paths if path.endswith(suffix)]
    return matching_paths

def replace_images_with_base64(directory_path):
    # 获取指定目录下的所有文件
    file_list = get_all_file_paths(directory_path)
    # 遍历每个文件
    for file_name in file_list:
        if file_name.endswith(".md"):
            
            file_path = os.path.join(directory_path, file_name)
            

            # print('file_path:', file_path)
            
            # 读取md文件内容
            with open(file_path, "r", encoding="utf-8") as file:
                md_content = file.read()

            # 搜索图片文件名并替换为base64字符串
            search_start_idx = 0
            while True:
                # 查找图片文件名的开始和结束位置
                start_idx = md_content.find("![[", search_start_idx)
                if file_path.endswith('团队运作机制和开发流程.md'):
                    print('start_idx:', md_content)
                if start_idx == -1:
                    break
                end_idx = md_content.find("]]", start_idx)
                if end_idx == -1:
                    break

                # 获取图片文件名
                image_file_name = md_content[start_idx+3:end_idx]
                print('image_name:', image_file_name)

                # 在指定目录中查找图片文件并转换为base64字符串
                image_path = get_paths_with_suffix(file_list, image_file_name)
                print('image_path:', image_path)
                if os.path.exists(image_path):
                    with open(image_path, "rb") as image_file:
                        image_data = image_file.read()
                    
                    # 将图片文件替换为base64字符串
                    image_base64 = base64.b64encode(image_data).decode("utf-8")
                    md_content = md_content[:start_idx] + "![](data:image/png;base64," + image_base64 + ")" + md_content[end_idx+2:]

                search_start_idx = end_idx + 2

            # 将替换后的内容写回md文件
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(md_content)
                


print('deal')

# 使用示例
directory_path = "/Users/lijinhong/codeAnt/lijinhong-blog/lijinhong-blog-hexo/"
replace_images_with_base64(directory_path)