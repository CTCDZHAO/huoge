import requests
class TestDemo:
    def test_get(self):
        r=requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code==200

    def test_query(self):
        payload={
            "level":1,
            "name":"ssdfsd",
        }
        r = requests.get("https://httpbin.testing-studio.com/get",params=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "ssdfsd",
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get",header={"h":"name"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "ssdfsd",
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.status_code)
        print(r.text)
        # print(r.json())
        assert r.status_code == 200
        assert r.json()['json']['level']==1

    def test_assert_json(self):
        r=requests.get("https://ceshiren.com/categories.json")
        print(r.json())
        # print(r.text)