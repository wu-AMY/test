import time

import pytest

from pythoncode.calculator import Calculater
import yaml

def get_datas():
    with open("testing/datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        add_number = datas["add"]["number"]
        add_smallnum = datas["add"]["smallnum"]
        add_ids = datas["add"]["ids"]
        return [add_number,add_smallnum,add_ids]


class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_datas()[1], ids=get_datas()[2])
    def test_add(self, get_calc, a, b, expect):
        # assert self.calc.add(a, b) == expect
        assert  get_calc.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 1), (20, 4, 5), (1, 0, 0), (0.1, 0.1, 1), (-1, -1, 1)])
    def test_div(self, a, b, expect,get_calc):
        assert get_calc.div(a, b) == expect

