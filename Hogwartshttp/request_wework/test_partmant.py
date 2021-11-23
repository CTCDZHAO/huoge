import requests

def test_token():
    res=None
    # 获取token
    corpid='wwe3077ee291d6a898'
    corpsecret='a-_vouMKTXFxX3G4yEWn8lsBNP2Cmq21oZWR24SFtJ0'
    r=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    # print(r.json()['access_token'])
    return r.json()['access_token']

def test_create():
    # 创建组织
    data={
        'name':'成都研发中心',
        'parentid':1,
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}',json=data)
    print(res.json())
def test_update():
    data={
        'id':2,
        "name":"chengdu"
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}',json=data)
    print(res.json())
def test_delete():
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2')
    print(res.json())
def test_get():
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}')
    print(res.json())