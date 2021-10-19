awesome-python3-webapp
======================

### server端准备工作
- 创建数据库，并写入初始化数据
```python3
# create database test data
# 1. create mysql
mysql -uroot -p < scheme.sql

# 2. make user data
python3 www/test.py
```
- server端需要提前定义好部署的目录结构
```shell
/
+- srv/
   +- awesome/       <-- Web App根目录
      +- www/        <-- 存放Python源码
      |  +- static/  <-- 存放静态资源文件
      +- log/        <-- 存放log
         +- access_log
         +- error_log
```

### 开发机准备工作
- pip requirements
```shell
# fabric版本太高，会报错
pip install fabric==1.14.0
```

- 如果server端的ssh不是默认的22端口，需要在fabfile.py配置
```shell
env.port = 4446
```

- fabric是基于py2, 所以确保pip是执行python2的
```shell
➜  awesome-peter git:(master) ✗ pip -V                    
pip 20.3.4 from /Library/Python/2.7/site-packages/pip (python 2.7)
```
