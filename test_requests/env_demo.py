"""
1. 需要二次封装requests，队请求进行定制化
2. 将请求的结构体的url从一个写死的IP地址改为一个（任意的）域名
3. 使用一个env配置文件，存放各个环境的配置信息
4. 然后将请求结构体中的url替换为‘env’配置文件中个人选择的url
5. 将env配置文件使用yaml进行管理
"""
import requests


class Api:
    data={
        'method':'',
        'url':'',

    }
    def send(self,data:dict):
        requests.request(method=,url=,json=)