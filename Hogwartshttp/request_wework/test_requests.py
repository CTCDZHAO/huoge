import random
import re

import pytest
import requests
@pytest.fixture(scope='session')
def test_token():
    corpid='wwe3077ee291d6a898'
    corpsecret='a-_vouMKTXFxX3G4yEWn8lsBNP2Cmq21oZWR24SFtJ0'
    r=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    # print(r.json()['access_token'])
    return r.json()['access_token']
def test_get(userid,test_token):
    r=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    return r.json()
@pytest.mark.parametrize('userid,name,mobile',[('2213123','zhao','15488989891')])
def test_create(userid,name,mobile,test_token):
    data={
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department":[1]
    }
    r=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}',json=data)
    print(r.json())
    return r.json()
def test_delete(userid,test_token):
    userid=userid
    r=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}')
    return r.json()
def test_update(userid,name,mobile,test_token):
    data={
        "userid":userid,
        "name":name,
        "mobile":mobile,
    }
    r=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}',json=data)
    return r.json()
def test_creat_data():
    data = [("wu123fff" + str(x), "zhangsan", "138%08d" % x) for x in range(20)]
    return data

@pytest.mark.parametrize("userid, name, mobile",test_creat_data())
def test_all(userid,name,mobile,test_token):
    # 可能发生创建失败
    try:
         assert "created" == test_create(userid, name, mobile,test_token)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)",e.__str__())[0]
            if re_userid.endswith("'") or re_userid.endswith('"'):
                re_userid=re_userid[:-1]
            assert "deleted" == test_delete(re_userid,test_token)['errmsg']
            assert 60111 == test_get(re_userid ,test_token)['errcode']
            assert "created" == test_create(userid, name, mobile,test_token)["errmsg"]

    # 可能发生userid不存在异常
    assert name == test_get(userid,test_token)['name']
    assert "updated" == test_update(userid, "xxxxxxx", mobile,test_token)['errmsg']
    assert "xxxxxxx" == test_get(userid,test_token)['name']
    assert "deleted" == test_delete(userid,test_token)['errmsg']
    assert 60111 == test_get(userid,test_token)['errcode']