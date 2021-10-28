import pytest
import yaml

from appium_xueqiu.page.app import App


class TestSearch():
    def setup(self):
        self.search = App().start().main().goto_market().go_to_search()
    # @pytest.mark.parametrize("name",["阿里巴巴","阿里巴巴-SW"])
    @pytest.mark.parametrize("name",yaml.safe_load(open("./test_search.yaml",encoding="utf-8")))
    def test_search(self,name):
        self.search.search(name)
        if self.search.is_choose(name):
           self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)