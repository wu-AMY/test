import json

import jsonpath as jsonpath
import requests
import pystache
class TestApi:
    def test_api_get(self):
        r = requests.get("http://httpbin.testing-studio.com/#/Auth/get_bearer")
        print(r.status_code)
        print(r.text)
        print(r.json)
        assert r.status_code == 200


    def test_query(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query_post(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

    def test_query_header(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={"h": "headers-demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_json(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    def test_post_pystache(self):
        data = {
            'level': '1',
            'name': 'chair'
        }
        template = pystache.render(
            open('template.mustache').read(),data
        )
        print(type(template))
        payload = {"level": 1, "name": "seveniruby"}
        print(type(payload))
        r = requests.post("http://httpbin.testing-studio.com/post", json=template)
        print(r.status_code)
        print(type(r.text))
        assert r.status_code == 200
        assert r.json()["json"] == template
        print(r.json())

    def test_paste(self):
        ip_set = set()  # 用于存储唯一的IP地址
        with open('a.txt', 'r') as file:
            print(file)
            for line in file:
                print(line)
                line = line.strip()  # 去除行首尾的空白字符
                parts = line.split()  # 使用默认的空白字符分割行内容

                if len(parts) >= 2:
                    ip_address = parts[0]  # 假设IP地址在第二个位置
                    ip_set.add(ip_address)

        # 打印唯一的IP地址
        for ip in ip_set:
            print(ip)



    def test_login(self):
        payload = {
            "accounts": "zz",
            "pass'word": "123456",
            "type": "username"
        }
        url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
        r = requests.post(url, json=payload)
        print(r.status_code)
        print(type(r.text))
        print(r.json())
        print(json.loads(r.text))


    def test_jsonpath_post(self):
        # data = {
        # "code": 1,
        # "msg": "success",
        # "data": {
        #     "list": None,
        #     "isLast": True,
        #     "timeRangeDesc": "只有近一个月的分享记录哦~",
        #     "effectDetailH5Url": "https://wxk.vip.com/promote_effect",
        #     "effectDescUrl": "https://mst.vip.com/_tdE7tjNIxghlOtWolbxbQ.php?wapid=mst_100019031&_src=mst&extra_banner=115019031&nova=1&nova_platform=1&mst_page_type=guide",
        #     "promoteTime": "2024-05-22 22:53:34",
        #     "effectDesc": "近7天出单数：0",
        #     "adCode": "hisGoods",
        #     "detailUrlApp": "https://m.vip.com/product-1710626677-6918163204848509525.html",
        #     "effectCount": 0
        #
        #     }
        # }
        data = {
            "store" : {
                "name" : "vip",
                "address" : "beijing",
            
                "book": [{"title": "python", "price": 100},
                         {"title": "java", "price": 200}
                         ],
                "user": {
                    "name": "seveniruby",
                    "age": 18
                    }

                }

        }
        res = jsonpath.jsonpath(data, '$..book[?(@.price >100)]')
        print(res)
        price = jsonpath.jsonpath(data, '$..book..price')
        print(price)






