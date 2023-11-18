# 防火墙
开启必要端口，关闭其他所有无用端口
# VPN
## shadowsocks 
shadowsocks 
**服务器安装shadowsocks镜像**
https://www.ktanx.com/blog/p/4807
docker run -d -p 54265:54265 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 54265 -k codeAnt123.+ -m aes-256-cfb

docker run -d -p 54264:54264 oddrationale/docker-shadowsocks -s 0.0.0.0 -p 54264 -k codeAnt123.+ -m aes-256-cfb

-   `-d`——容器启动后会进入后台
-   `-p（第一个）`——指定要映射的端口，使用的格式是`hostPort:containerPort`，即本地的 54285 端口映射到容器的 54285 端口
-   `-s`——客户端服务器IP 
-   `-p（第二个）`——代理端口
-   `yourpasswd`——你的密码
-   `-m`——加密方式
**开启端口**
```
firewall-cmd --zone=public --add-port=54265/tcp --permanent
firewall-cmd --reload
命令含义：

–zone #作用域

–add-port=9200/tcp #添加端口，格式为：端口/通讯协议

–permanent #永久生效，没有此参数重启后失效

注意：添加端口后，必须用命令firewall-cmd --reload重新加载一遍才会生效
```
**shadowsocks客户端**
https://github.com/orgs/shadowsocks/repositories?page=1
```
mac安装
要在 macOS 13 M1 芯片上安装 SS（Shadowsocks）客户端，您可以按照以下步骤进行操作：

1.打开终端应用程序

2.使用Homebrew包管理器安装SS客户端。 如果您还没有安装Homebrew，请在终端中运行以下命令安装它：

复制代码

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

3.一旦安装了Homebrew，您可以运行以下命令来安装SS客户端：

复制代码

`brew install shadowsocks-libev`

4.等待安装完成之后，您可以通过以下命令启动SS客户端：

复制代码

`ss-local -c /usr/local/etc/shadowsocks-libev.json`

现在，您已经成功地在macOS 13 M1芯片上安装和启动了SS客户端。

To restart shadowsocks-libev after an upgrade:

  brew services restart shadowsocks-libev

Or, if you don't want/need a background service you can just run:

  /opt/homebrew/opt/shadowsocks-libev/bin/ss-local -c /opt/homebrew/etc/shadowsocks-libev.json
```
## shadowsocks-R
https://hub.docker.com/r/teddysun/shadowsocks-r
可了解
# 通过ng做网关

docker pull cym1102/nginxwebui:latest

docker run -itd --restart=always --name=nginxWebUI  -v /home/nginxWebUI:/home/nginxWebUI -e BOOT_OPTIONS="--server.port=8080" --privileged=true --net=host  cym1102/nginxwebui:latest /bin/bash

开放8080端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent
firewall-cmd --reload

firewall-cmd --zone=public --remove-port=54264/tcp --permanent
firewall-cmd --zone=public --remove-port=54265/tcp --permanent

l30013501
ljh199811..++..++

# chatGPT
https://zhuanlan.zhihu.com/p/618974540?utm_id=0
```yaml
version: '3'
 
 services:
   app:
     image: chenzhaoyu94/chatgpt-web # 总是使用 latest ,更新时重新 pull 该 tag 镜像即可
     ports:
       - 3002:3002
     environment:
 # 二选一 这里填上你自己的api_key即可
       OPENAI_API_KEY: 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
 # 二选一
 # OPENAI_ACCESS_TOKEN: xxx
 # API接口地址，可选，设置 OPENAI_API_KEY 时可用
 # OPENAI_API_BASE_URL: xxx
 # API模型，可选，设置 OPENAI_API_KEY 时可用，https://platform.openai.com/docs/models
 # gpt-4, gpt-4-0314, gpt-4-32k, gpt-4-32k-0314, gpt-3.5-turbo, gpt-3.5-turbo-0301, text-davinci-003, text-davinci-002, code-davinci-002
       OPENAI_API_MODEL: gpt-3.5-turbo
 # 反向代理，可选
 # API_REVERSE_PROXY: xxx
 # 访问权限密钥，可选 推荐设置，这样就只有你自己和知道你的密钥的人可以访问这个服务，可以减少不必要的损失
       AUTH_SECRET_KEY: ljh0320
 # 每小时最大请求次数，可选，默认无限
       MAX_REQUEST_PER_HOUR: 0
 # 超时，单位毫秒，可选
       TIMEOUT_MS: 60000
 # Socks代理，可选，和 SOCKS_PROXY_PORT 一起时生效
 # SOCKS_PROXY_HOST: xxx
 # Socks代理端口，可选，和 SOCKS_PROXY_HOST 一起时生效
 # SOCKS_PROXY_PORT: xxx
 # HTTPS 代理，可选，支持 http，https，socks5
 # HTTPS_PROXY: http://xxx:7890
```