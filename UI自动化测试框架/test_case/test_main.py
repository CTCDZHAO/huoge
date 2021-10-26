import pytest
import yaml

from page.app import App


class TestMain:
    # @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    # def test_main(self):
    #     app=App()
    #     app.start().main().go_to_search()
    #     # print(value1)
    #     # print(value2)
    def test_windows(self):
        app=App()
        app.start().main().go_to_windows()
