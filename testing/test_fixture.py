import pytest
@pytest.fixture()
def loginL():
    print('步骤一：登录')
    a="返回值"
    yield a

class TestDemo:
    def test_a(self,loginL):
        print('步骤二：测试A',loginL)

    def test_b(self):
        print('步骤二：测试B')

    def test_c(self):
        print('步骤二：测试C')

# if __name__ == '__main__':
#     pytest.main()