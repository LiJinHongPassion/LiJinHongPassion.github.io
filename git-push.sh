#!/usr/bin/env sh
# 将![[图片文件名]]转化为base64的md图片格式
python3.10 deal_img.py
#仅仅上传到oneDrive，在github中标记为ignore
python3.10 deal_only_drive.py
# 给文章加标题，最多3级目录
python3.10 deal_title_number.py
git add .gitignore
git commit -m 'update ignore'
# 清除所有的文件追踪（这样才能是gitignore生效，否则有些ignore会失效）
git rm -r --cached .
git commit -m 'rm all file'
git push

# 推送所有文章
git add .
npx hexo generate
git commit -m 'update'
git push
