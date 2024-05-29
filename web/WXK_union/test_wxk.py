from web.WXK_union.index_page import IndexPage


class TestWxk:


    def test_register(self,get_index):
        get_index.goto_register().register("17857411480", "abcd1234")

    def test_login(self, get_index):
        get_index.goto_cookies_login().scan()

