import requests

# 传入数据可能是字典
class BaseApi:
    def send(self,data):
        return  requests.request(**data)#解开字典