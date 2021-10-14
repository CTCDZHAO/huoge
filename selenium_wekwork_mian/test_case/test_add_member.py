from time import sleep

from selenium_wekwork_mian.page.main import Main


class TestAddMember:
    def setup(self):
        self.main=Main()

    def test_ademember(self):
        add_member=self.main.goto_add_memeber()
        add_member.add_member()
        sleep(3)
        assert "username" in add_member.get_member()