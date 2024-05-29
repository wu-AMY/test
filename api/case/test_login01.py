import json

import allure
import pytest
import requests

from api.api_keyword.api_key import apiKey


class TestLogin:

    @pytest.mark.parametrize("data1", [{"username": "amy_test", "pwd": "test1234", "export": "登录成功"}])
    @allure.title("登录成功case1")
    def test_login(self, data1):
        print(data1)
        api = apiKey()
        data = {
            "accounts": data1["username"],
            "pwd": data1["pwd"],
            "type": "username"
        }
        gc = {
            "application": "app",
            "application_client_type": "weixin"
        }

        url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
        res = api.post(url=url, data=data, params=gc)
        result = api.get_jsonpath(res.text, "$..token")
        msg = api.get_jsonpath(res.text, "$..msg")
        token = json.loads(res.text)["data"]["token"]
        assert token == result

        assert msg == data1["export"]
        print(res.text)
        print(result)
        print(token)


    def test_login_02(self):
        #01执行登录获取token
        with allure.step("01执行登录获取token"):
            api = apiKey()
            data = {
                "accounts": "amy_test",
                "pwd": "test1234",
                "type": "username"
            }
            gc = {
                "application": "app",
                "application_client_type": "weixin"
            }

            url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
            res = api.post(url=url, data=data, params=gc)
            result = api.get_jsonpath(res.text, "$..token")
            token = json.loads(res.text)["data"]["token"]

        #02加入购物车
        with allure.step("02加入购物车"):
            data_shop = {

                "goods_id": 2,
                "spec": [{"type": "套餐", "value": "套餐一"},
                         {"type": "颜色", "value": "金色"},
                         {"type": "容量", "value": "32G"}
                         ],
                "stock": 1

            }
            param_shop = {
                "application": "app",
                "application_client_type": "weixin",
                "token": token
            }
            url_shop = "http://shop-xo.hctestedu.com/index.php?s=api/cart/save"
            res_shop = api.post(url=url_shop, data=data_shop, params=param_shop)
            print(res_shop.json())
            assert res_shop.json()["msg"] == "加入成功"

        with allure.step("03查询购物车"):
            url_shop_cart = "http://shop-xo.hctestedu.com/index.php?s=api/cart/index"
            res_shop_car = api.get(url=url_shop_cart, params=param_shop)
            print(res_shop_car.json())
            cart_list = api.get_jsonpath(res_shop_car.text, "$..id")
            print(cart_list)

        with allure.step("04提交订单"):
            data_order = {
                "goods_id": 2,
                "buy_type": "cart",
                "stock": 1,
                "spec" : "",
                "ids": cart_list,
                "address_id": 921,
                "payment_id": 4,
                "user_note": "",
                "site_mode": 0
            }
            url_shop_order ="http://shop-xo.hctestedu.com/index.php?s=api/buy/add"

            res_shop_order = requests.post(url=url_shop_order, data=data_order, params=param_shop)
            print(res_shop_order.text)
            order_id = api.get_jsonpath(res_shop_order.text, "$..order_ids")
            print(int(order_id[0]))

        with allure.step("05查询订单"):
            data_order_query = {
                "id": int(order_id[0])
            }
            url_order_query = "http://shop-xo.hctestedu.com/index.php?s=api/order/detail"
            res_order_query = api.get(url=url_order_query, params=param_shop, data=data_order_query)
            print(res_order_query.text)






