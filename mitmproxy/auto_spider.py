# C:\Users\yueliuk\AppData\Local\Google\Chrome\Application\chrome.exe  --proxy-server=127.0.0.1:8080  --ignore-certificate-errors

# https://admin.baitoujia.com.cn/bax/static/img/logo_mini.ef8c25e.png HTTP/2.0
#      << HTTP/2.0 200 OK 15.6k
# 200
# 127.0.0.1:63655: POST https://admin.baitoujia.com.cn/api/baxter/menu/getMenusList HTTP/2.0
#      << HTTP/2.0 200 OK 9.6k
# 200
# 127.0.0.1:63655: POST https://admin.baitoujia.com.cn/api/baxter/dictionary/getTagList
# mitmdump -s E:\pythonProject\k8s\mitmproxy/auto_spider.py
from mitmproxy import ctx
import re


def request(flow):
    # 获取请求对象
    request = flow.request
    # 实例化输出类
    info = ctx.log.info
    # 打印请求的url
    if len(re.findall('http.*api', request.url)) > 1:
        info(request.url)
        fp = open("log.txt", 'a+', encoding='utf-8')
        fp.write(str(request.url) + '\n')
    # 打印请求方法
    # info(request.method)
    # # 打印host头
    # info(request.host)
    # # 打印请求端口
    # info(str(request.port))
    # # 打印所有请求头部
    # info(str(request.headers))
    # # 打印cookie头
    # info(str(request.cookies))


# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    # 获取响应对象
    response = flow.response
    # 实例化输出类
    info = ctx.log.info
    # 打印响应码
    # info(str(response.status_code))
    # # 打印所有头部
    # info(str(response.headers))
    # # 打印cookie头部
    # info(str(response.cookies))
    # # 打印响应报文内容
    # info(str(response.text))

#
# if __name__ == '__main__':
#     print(len(re.findall('http.*ap1i', 'https://admin.baitoujia.com.cn/api/baxter/menu/getMenusList')))
