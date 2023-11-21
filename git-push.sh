#!/usr/bin/env sh
python3.10 deal_img.py
python3.10 deal_only_drive.py
git rm -r --cached *
git add .gitignore
git commit -m 'update ignore'
git add .
git commit -m 'update'
git push
