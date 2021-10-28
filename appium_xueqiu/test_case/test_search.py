import pytest

from appium_xueqiu.page.app import App


class TestSearch():
    def setup(self):
        self.search = App().start().main().go_to_market().go_to_search()
    # @pytest.mark.parametrize("name",["阿里巴巴","京东","阿里巴巴-SW"])
    def test_search(self):
        self.search.search("阿里巴巴")
        if self.search.is_choose("阿里巴巴"):
           self.search.reset("阿里巴巴")
        self.search.add("阿里巴巴")
        assert self.search.is_choose("阿里巴巴")