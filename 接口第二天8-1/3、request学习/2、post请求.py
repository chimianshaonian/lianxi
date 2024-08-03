# 导包
import json

import requests

# post传参有两种方式：表单、json

# 1、表单传参
# 准备接口
# url1 = "https://wanandroid.com/user/login"
# # 准备数据
# payload = {"username": "ymw001", "password": "123456"}
# # 进行请求
# res = requests.post(url= url1,data=payload)
# # 查看结果
# # print(res.text)
# # 如果响应体式json格式，可以直接转化为字典
# res1 = res.json()
# print(res1)

# -------------------------------
# 2、json传参
# 准备接口
url1 = 'http://httpbin.org/post'
# 准备数据
payload = {"username": "ymw001", "password": "123456"}

# # 方式一：将字典转化为json，进行传参，传递给形参data，用dumps方法
# m = json.dumps(payload)
# print(m)
# # 进行请求
# res = requests.post(url=url1,data=m)
# # 查看结果
# print(res)

# 方式二：直接把字典格式的数据转递给新参：json
res = requests.post(url=url1,json=payload)
# 查看结果
print(res.text)
print(res.json())  # 如果响应体式json格式，可以直接转化为字典
