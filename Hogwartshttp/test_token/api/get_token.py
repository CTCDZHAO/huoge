from string import Template

import yaml

from test_token.api.base_api import BaseApi
import yaml

class GetToken(BaseApi):
    _corpid="wwe3077ee291d6a898"
    _corp_secret="a-_vouMKTXFxX3G4yEWn8lsBNP2Cmq21oZWR24SFtJ0"
    def template(self):
        with open('../api/get_token.yaml') as f:
            data={
                "corpid" : "wwe3077ee291d6a898",
            "corpsecret" : "a-_vouMKTXFxX3G4yEWn8lsBNP2Cmq21oZWR24SFtJ0"
            }
            re=Template(f.read()).substitute(data)
            return yaml.safe_load(re)
    def get_token(self):
        req=self.template()
        r=self.requests_http(req)
        return r
if __name__ == '__main__':
    GetToken().template()
    # r=GetToken().get_token()
    # print(r.json())
