class Tag:
    def token():
        self.token=get_token()
    def get():
        data={
        'url':'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN',
       'params':{
       "tagname": "UI",
       "tagid": 12
            }
        }
