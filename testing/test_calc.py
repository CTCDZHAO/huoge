# -*-coding:utf-8-*-
import pytest
import yaml
from handle.handle_yaml import testdata
from apis.calc import Calc
from decimal import Decimal#计算浮点数
import os
def steps():
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(dirname, r'testing\steps.yaml')) as f:
        return yaml.safe_load(f)


#         # print(yaml.safe_load(f))

class TestCalc:
    def setup(self):
        self.calc = Calc()
        self.testdata=testdata()
    # @pytest.mark.parametrize("a,b,expected", [
    #     (5, 5, 10),
    #     (-1, 0, -1),
    #     (0.5, 0.1, 0.6),
    #     (123456, 9455, 222222),
    #     ("a", 1, 'can only concatenate str (not "int") to str'),
    #     ([1], 1, 'can only concatenate list (not "int") to list'),
    #     (None, 1, "unsupported operand type(s) for +: 'NoneType' and 'int'")
    # ])
    # @pytest.mark.run
    # def test_add(self, a, b, expected):
    #     # a,b 为整数或浮点数
    #     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    #         result = self.calc.add(a, b)
    #         assert result == expected
    #     # a,b 为其他数据类型时
    #     else:
    #         with pytest.raises(TypeError):
    #             self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expected",testdata())
    def test_add_tow(self, a, b, expected):
        # a,b 为整数或浮点数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.add(a, b)
            assert result == expected
        # a,b 为其他数据类型时
        else:
            with pytest.raises(TypeError):
                self.calc.add(a, b)
    # 配置step
    @pytest.mark.parametrize("a,b,expected", testdata())
    def test_add_first(self,a, b, expected,):
        steps1=steps()
        for step in steps1:
            print('step======>',step)
            if 'add' ==step:
                result = self.calc.add(a, b)
            elif 'add1'==step:
                result = self.calc.div(a, b)
        print(result)
        assert result==expected
    # @pytest.mark.parametrize("a,b,expected", [
    #     (10, 5, 2),
    #     (7, 3, 7 / 3),
    #     (-1, 1, -1),
    #     (2, 0.1, 20.0),
    #     (0, 1, 0),
    #     (0, 0, "division by zero")
    # ])
    # def test_div(self, a, b, expected):
    #     # 除数为0
    #     if b == 0:
    #         with pytest.raises(ZeroDivisionError):
    #             self.calc.div(a, b)
    #     # a,b 为整数或浮点数
    #     elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
    #         result = self.calc.div(a, b)
    #         assert result == expected
    #     # a,b 为其他数据类型
    #     else:
    #         with pytest.raises(TypeError):
    #             self.calc.div(a, b)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_calc.py'])
