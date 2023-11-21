#!/usr/bin/env sh
python3.10 deal_img.py
python3.10 deal_only_drive.py
git add .gitignore
git commit -m 'update ignore'
git rm -r --cached .
git commit -m 'rm all file'
git push

git add .
#npx hexo generate
git commit -m 'update'
git push
