import json
import re
import time

import requests
import os
import io
from line_profiler import LineProfiler
from functools import wraps
import pandas as pd

src_file_path = '''E:\\txt\\26008.txt'''
target_file_path = '''E:\\txt\弃宇宙.txt'''


# 查询接口中每行代码执行的时间
def func_line_time(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        func_return = f(*args, **kwargs)
        lp = LineProfiler()
        lp_wrap = lp(f)
        lp_wrap(*args, **kwargs)
        lp.print_stats()
        return func_return

    return decorator


def replaceSigale(src_path, target_path):
    if os.path.exists(target_path):
        os.remove(target_path)
    with io.open(target_file_path, "w+", encoding='utf-8') as f1:
        with io.open(src_path, 'r', encoding='utf-8') as f2:
            str = f2.read(1024 * 8)
            while len(str) > 0:
                str = re.sub(r'^.*p>|[（\[\(].*[\)\]）]|7017k', '', str)
                f1.write(str)
                str = f2.read(1024 * 8)
            f1.close()
            f2.close()


#
# if __name__ == '__main__':
#     replaceSigale(src_file_path, target_file_path)

http_novel = 'http://www.ujxsw.com/'


class Novel:
    __http_url = ''
    __local_path = ''
    __chapter_list_dic = []

    def __init__(self, http_url, local_path, __chapter_list_dic):
        self.__http_url = http_url
        self.__local_path = local_path
        self.__chapter_list_dic = __chapter_list_dic
    #
    # def getHtmlLocal(self, htmlName='1.html', lambda requests: get()) :
    # local_path = self.__local_path + htmlName
    # if os.path.exists(local_path):
    #     os.remove(local_path)
    # with open(local_path, 'w+', encoding='utf-8') as loc:
    #     loc.write()


# @func_line_time
def writeFile(filepath, data):
    if os.path.exists(filepath):
        os.remove(filepath)
    with open(filepath, 'w+', encoding='utf-8') as loc:
        loc.write(data)


http = "http://www.ujxsw.com/"


# if __name__ == '__main__':
#     # print(os.getcwd())
#     data = requests.get(http + "read/26008/")
#     txt = data.content.decode('utf-8')
#     regx = re.compile(r"/(?P<value>read/26008/.*html).*(?P<key>第\W+章)", re.A)
#     chapeter_list_iter = re.finditer(regx, txt)
#
#     chapeter_dic = {item.groupdict()['key']: item.groupdict()['value'] for item in chapeter_list_iter}
#     chapeter_list = list(chapeter_dic.keys())
#     url_list = [http + '/read/' + chapeter_dic[item] for item in chapeter_dic if
#                 chapeter_list[len(chapeter_list) - 10:].count(item) > 0]
#     for item in url_list:
#         text = requests.get(http_novel).text
#         chat = re.findall('<h3 class="zhangj">.*</h3>|.*<br />', text)
#         list_index = [1, len(chat) - 4, len(chat) - 2, len(chat) - 1]
#         for index, c in enumerate(chat):
#             if list_index.count(index) == 0:
#                 txt = txt + re.sub(regx, '', c) + '\n'  # + str(index)
#     print(txt)
#     # with io.open(target_file_path, 'a', encoding='utf-8') as file:
#     #     file.write(txt)
#     #     file.close()


@func_line_time
def novel(web_address='', all_html='', all_pattern='', chapter_pattern='', revert_len=-1, target_path='', **kwargs):
    data = requests.get(web_address + all_html)

    # data = requests.get("http://m.fanqianxs.com/html/148895/17016572.html")
    # print(file.replace('\\', '/'))
    d1 = re.finditer(all_pattern, data.text)
    d2 = [item.groupdict() for item in d1]
    # print(d2[-90:])
    txt = ''
    for item in d2[revert_len:]:
        url = web_address + item['url']
        resp = requests.get(url)
        content = re.findall(chapter_pattern, resp.text)
        for t1 in content:
            txt = txt + re.sub(r'（.*）', '', t1) + '\n'
    writeFile(target_path, txt)


if __name__ == '__main__':
    param = {'web_address': 'http://m.fanqianxs.com',
             'all_html': '/book/qiyuzhou/all.html',
             'all_pattern': '\<li\>\<a href\=\"(?P<url>.*).*\"\>(?P<chapter>[^（）\n]*).*\<\/a\>\<\/li\>',
             'revert_len': -20,
             'target_path': src_file_path,
             'chapter_pattern': '(?<=id="nr_title">).*(?=</div>)|(?<=<p>)[^.()（）/n]*(?=</p>)'
             }
    novel(**param)

    # df1 = pd.DataFrame(json_data)
    # df1[['companyId', 'companyName', 'payType', 'amount']].groupby('companyId').sum()

    # headers = {'Content-Type': 'application/json',
    #            'Cookie': 'XXL_JOB_LOGIN_IDENTITY=7b226964223a312c22757365726e616d65223a2261646d696e222c2270617373776f7264223a226531306164633339343962613539616262653536653035376632306638383365222c22726f6c65223a312c227065726d697373696f6e223a6e756c6c7d'}

    # res = requests.get(
    #     url='http://10.32.26.32:2000/xxl-job-admin/jobinfo/pageList?jobGroup=1&jobDesc=&executorHandler=&start=0&length=100',
    #     headers=headers)
    # data = json.loads(res.content.decode('utf-8'))
    #
    # pd.DataFrame(data.)
    # print()

    # print(re.sub(r'（.*）', '', '第七十二章 前往玉启星（324124af的撒）'))
    #  C:\Users\yueliuk\AppData\Roaming\Python\Python38\Scripts
    # web_address = 'http://m.fanqianxs.com';
    # # data = requests.get("https://kone.kingdee.com/certexam/answer?exam=1418101187734938624&source=A")
    # data = requests.get("http://m.fanqianxs.com/book/qiyuzhou/all.html")
    #
    # # data = requests.get("http://m.fanqianxs.com/html/148895/17016572.html")
    # # print(file.replace('\\', '/'))
    # d1 = re.finditer(r'\<li\>\<a href\=\"(?P<url>.*).*\"\>(?P<chapter>[^（）\n]*).*\<\/a\>\<\/li\>', data.text)
    # d2 = [item.groupdict() for item in d1]
    # # print(d2[-90:])
    # txt = ''
    # for item in d2[-90:]:
    #     url = web_address + item['url']
    #     resp = requests.get(url)
    #     content = re.findall(r'(?<=id="nr_title">).*(?=</div>)|(?<=<p>)[^.()（）/n]*(?=</p>)', resp.text)
    #     for t1 in content:
    #         txt = txt + t1
    # writeFile(src_file_path, txt)
