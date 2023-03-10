#!/bin/bash

## 使用方法：修改hardhat_create.sh 权限 chmod 777 hardhat_create.sh
## 运行： ./hardhat_create.sh  项目目录   例如： ./hardhat_create.sh ./project-example

echo "开始创建项目：$1";
mkdir -p $1
cd $1

## git 操作
git init

wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/.gitignore
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/README.md
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/gitlab-ci.yml
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/.env.sample
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/.solcover.js
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/.soliumrc.json
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/CHANGLOG.md
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/LICENSE
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/slither.config.json
wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/process_config


chmod 777 process_config
git add .
git commit -m "init"
git branch 1.0.0
git checkout 1.0.0

## hardhat 创建
npm init
npm install --save-dev hardhat
npx hardhat
./process_config ./package.json

mkdir example
mv  scripts tasks

rm process_config

wget -N https://raw.githubusercontent.com/blockchain-pro/xd-share/main/hardhat.config.js

echo "创建项目完成";


