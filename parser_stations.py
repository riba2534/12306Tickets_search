#本程序是为了解析出每一个火车站的代码
#使用方法是使用本程序把输出结果重定向到ststion.py文件里面
import requests
import re
from pprint import pprint
def main():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
    r=requests.get(url,verify=False)         #后面的参数可以去除https验证
    r.encoding=r.apparent_encoding
    pattern=u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  #正则表达式匹配
    result=re.findall(pattern,r.text)
    pprint(dict(result),indent=4)

if __name__ == '__main__':
    main()
