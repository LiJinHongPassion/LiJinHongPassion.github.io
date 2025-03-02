#!/usr/bin/env sh
# github作为主仓库
git remote add origin git@github.com:LiJinHongPassion/LiJinHongPassion.github.io.git
# gitee作为备份仓库，目的是为了更快速的访问，因为github有可能会打不开
# git remote add backup git@gitee.com:LiJinHongPassion/lijinhong-hexo-blog.git

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
# 推送
git push origin
# git push backup

echo '如果卡住不动了，记得下载oneDriver里面所有的文件到本地，因为oneDriver的机制会删除本地不常用的文件，保留远端文件'

# 推送所有文章
git add .
npx hexo generate
git commit -m 'update'
# 推送
git push origin
# git push backup
