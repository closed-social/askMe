# askMe
匿名提问箱

## 部署指南

### 准备工作

+ Python3

+ 若干依赖包(暂时没requirement.txt，看到缺啥装啥吧)

+ 在任意Mastodon站点上创建一个应用(建议用一个独立的bot账号创建应用)
  
  + 勾选至少read:accounts和write:statuses权限

  + "跳转URI"一项添加 \<WORK\_URL\>/askMe/auth(示例: https://closed.social/askMe/auth )

  + 获得应用ID、应用密钥、访问令牌，

### 配置

`DOMAIN` 改为实际的mastodon站点

`WORK_URL` 改为提问箱计划使用的网址

`CLIENT_ID`、`CLIENT_SEC`、`token` 改为应用的id、秘钥、令牌，或写在文件中

`BOT_NAME` 改为bot的username（仅影响回答内容的显示）

### 运行

+ 开发环境: `$ python3 ask.py`

+ 生产环境: 建议使用[uwsgi](https://flask.palletsprojects.com/en/2.0.x/deploying/uwsgi/)（可使用pip安装）

仅供参考的配置文件：

ask.ini

```
[uwsgi]
wsgi-file = ask.py
callable = app
master = true
processes = 1
threads = 3

chdir = /home/bots/web/askMe/
socket = /tmp/ask.sock
logto = /home/bots/web/log/ask.log
pidfile = /home/bots/web/pid/ask.pid
chmod-socket = 666
```

`$ uwsgi ask.ini &` 或使用emperor管理多个ini

(如果不使用emperor，建议 `$ uwsgi --touch-reload=ask.ini ask.ini &`, 修改代码后编辑ask.ini或直接`$ touch ask.ini` 自动重新加载)
