"""
1、接口地址
    <1-1>协议：域名/路径（path）
        如:https://www.baidu.com/use/log
        域名：https://www.baidu.com
        路径：/use/log
    <1-2>接口协议：http协议
        1、请求头：request header
            请求行：请求地址、请求方式、协议版本
            cookie/token/seesion:表示身份信息
            userAgent:表示客户端访问接口的来源方式/工具
            content—Type：表示post接口入参的请求方式
                分为：表单:application/www-from-
                    json:application/json
        2、请求体：request body
            请求参数
        3、响应头：response header
            状态行：http status code：表示请求结果装填
                状态码有如下：
                    2XX：请求成功，但不代表业务逻辑处理成功
                    3XX：重定向
                    4XX：客户端错误导致--请求的资源在服务端不存在、请求接口错误
                    5XX：服务端错误

            conten—Type：同请求头里的conten—Type  表示post接口入参的请求方式
            服务器返回的cookie
        4、响应体：response body
    <1-3>请求方式：get、post、put、delete等
    <1-4>入参、出参
问题1：http和hettps区别
    1、端口：http--80；https--443
    2、安全性：https更安全
    3、是否免费：https需要购买证书
问题2：get与post的区别
    1、参数：get的在url中；post的在表单中--body
    2、安全性：post安全性更好
    3、提交内容：get提交参数长度有限；post表单可以发送更多内容的参数
"""

# 导包
import requests
# 准备接口
url1 = 'https://www.kuaidi100.com/query'
# 准备数据
payload = {"type":"shunfeng","postid":"SF1409812533370"}
# 进行请求
res = requests.get(url=url1,params=payload)
# 查看结果
# print(res)
# # 查看请求头
# print(res.request.headers)
# # 查看请求体
# print(res.request.body)
# # 查看响应头
# print(res.headers)
# # 查看响应体
# print(res.text)
# # 查看状态码
# print(res.status_code)
# 查看cookie
# print(res.cookies)
# print(res.cookies.get_dict())   # 转换为字典
# 如果响应体式json格式，可以直接转化为字典
res_dict = res.json()
# print(type(res_dict))
print(res_dict)





