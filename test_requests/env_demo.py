"""
1. ��Ҫ���η�װrequests����������ж��ƻ�
2. ������Ľṹ���url��һ��д����IP��ַ��Ϊһ��������ģ�����
3. ʹ��һ��env�����ļ�����Ÿ���������������Ϣ
4. Ȼ������ṹ���е�url�滻Ϊ��env�������ļ��и���ѡ���url
5. ��env�����ļ�ʹ��yaml���й���
"""
import requests


class Api:
    data={
        'method':'',
        'url':'',

    }
    def send(self,data:dict):
        requests.request(method=,url=,json=)