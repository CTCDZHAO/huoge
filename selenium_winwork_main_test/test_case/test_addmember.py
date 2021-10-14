from time import sleep

from selenium_winwork_main_test.page.main import Main


class TestAddMember:
    def setup(self):
        self.main=Main()
    def test_ademember(self):
        add_member = self.main.goto_addmember()
        add_member.add_member()
        assert  add_member.get_member('username')