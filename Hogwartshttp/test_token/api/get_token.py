import yaml

from test_token.api.base_api import BaseApi
import yaml

class GetToken(BaseApi):
    # _corpid="wwe3077ee291d6a898"
    # _corp_secret="a-_vouMKTXFxX3G4yEWn8lsBNP2Cmq21oZWR24SFtJ0"
    def get_token(self):

        # req={
        #     'method':'get',
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     "params":{
        #         "corpid":self._corpid,
        #         "corpsecret":self._corp_secret
        #     }
        # }
        req=yaml.safe_load(open('../api/get_token.yaml'))
        r=self.requests_http(req)
        return r
if __name__ == '__main__':
    r=GetToken().get_token()
    print(r.json())