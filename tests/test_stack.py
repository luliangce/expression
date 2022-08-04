from unittest import TestCase

from expression.operators import Add
from expression.parser import parse


class TestStack(TestCase):

    def test_add(self):
        self.assertEqual(Add().execute(1, 2), 3)

    def test_expression(self):

        exps = [
            "-1",
            "1+-1",
            "1 + 1",
            "(1+2)*3",
            "1-1",
            "1*1",
            "1*2",
            "1/2",
            "0.5*100",
            "0*0",
            "",
            "2*(1+1)",
            "2*((1+5)*10)",
            "3 * 1 % 2",
            "2**2",
            "2^2",
        ]

        for exp in exps:
            stack = parse(exp)
            r = stack.calc()
            self.assertEqual(r, eval(exp.replace("^", "**")) if exp else 0)
