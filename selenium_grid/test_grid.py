from  selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
class TestGrid:
    def test_grid(self):
        hub_url="http://127.0.0.1:4444/wb/hub"
        capability=DesiredCapabilities.CHROME.copy()

