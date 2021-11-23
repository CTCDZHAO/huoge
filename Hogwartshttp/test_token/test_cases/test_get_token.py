from test_token.api.get_token import GetToken


class TestToken:

    def setup(self):
        self.gettoken=GetToken()
    def test_get_token(self):
        print(self.gettoken.get_token().json())
        assert self.gettoken.get_token().json()['errcode']==0