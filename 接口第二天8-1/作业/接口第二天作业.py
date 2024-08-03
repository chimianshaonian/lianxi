# 1-http协议的组成，状态码含义；
"""
http协议的组成
    1、请求头：request header
        请求行：请求地址、请求方式、协议版本
        cookie/token/sossion:身份信息
        userAnget:客户端请求接口的访问来源（什么端、系统、浏览器啥的）
        connect—Type:表示post接口入参的方式
            分为：表单（application/www-from-）
                json(application/json)
    2、请求体：request body
        请求参数
    3、响应头：response header
        状态行：请求结果的装填
            状态码：2XX：请求成功，但不代表业务逻辑处理成功
                  3XX：重定向
                  4XX：客户端错误（接口错误、客户端访问的资源在服务器不存在）
                  5XX：服务端错误
            connect—Type：post的入参方式
    4、响应体：response body
"""
# 2-get和post区别
"""
1、参数：get是在url中，post是在表单中
2、安全性：post更为安全
3、提交内容：get请求参数长度有限制：post可以在表单内提交更多的内容
"""


# 3-cookie和session区别
"""
1、存储位置：
        cookie存在用户侧；
        session在服务端侧
2、安全性：
        cookie因是在用户侧，容易给篡改；
        session更安全，因在服务端
3、有效期：
        cookie可以设置具体过期时间
        session在用户关闭端或长时间不活跃后失效
4、内容：
        cookie:不敏感的数据
        session：用户比较私密的数据
5、性能：
        session对服务端性能有影响，如双11、618

"""

# 4 http和https的区别
"""
1、端口：http--80，https--443
2、安全性：https更安全
3、是否免费：https需要购买相应的证书
"""
# 5 作业restful风格的接口
"""
1、客户端-服务端分离：明确区分客户端和服务端
2、统一接口：无论接口要做什么，都需要通过相似的步骤来完成
3、可缓存：如有些信息不经常改变，可以缓存在电脑上，不用每次都需要单独下线
"""










