import json

import allure
import requests
from requests import request
import jsonpath as jsonpath


class apiKey:
    @allure.step("发送get 请求")
    def get(self, url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)

    @allure.step("发送post请求")
    def post(self, **kwargs):
        return requests.post(**kwargs)


    #基于jsonpath获取数据的关键字
    def get_jsonpath(self, json_data, jsonpath_exp):
        """
        :param json_data: json数据
        :param jsonpath_exp: jsonpath表达式
        :return:
        """
        dict_data = json.loads(json_data)
        result = jsonpath.jsonpath(dict_data, jsonpath_exp)
        if result:
            return result[0]
        else:
            return None
if __name__ == '__main__':
    api = apiKey()
    data ={
        "accounts":"amy_test",
        "pwd":"test1234",
        "type": "username"
    }
    gc = {
        "application":"app",
        "application_client_type": "weixin"
    }

    url ="http://shop-xo.hctestedu.com/index.php?s=api/user/login"
    res = api.post(url= url, data=data, params=gc)
    result = api.get_jsonpath(res.text, "$..token")
    rest = json.loads(res.text)["data"]["token"]
    print(res.text)
    print(result)
    print(rest)