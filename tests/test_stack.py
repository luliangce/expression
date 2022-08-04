from unittest import TestCase

from expression.operators import Add
from expression.parser import parse


class TestStack(TestCase):

    def test_add(self):
        self.assertEqual(Add().execute(1, 2), 3)

    def test_expression(self):

        pure_expressions = [
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
            "1+2*3+4",
        ]

        for exp in pure_expressions:
            stack = parse(exp)
            r = stack.calc()
            self.assertEqual(r, eval(exp.replace("^", "**")) if exp else 0)

        with_vars = [("a+b*3+4", {
            "a": 1,
            "b": 2,
        }), ("x*y", {
            "x": 100,
            "y": -32,
        })]
        for exp in with_vars:
            stack = parse(exp[0])
            result = stack.calc(**exp[1])
            self.assertEqual(result, eval(exp[0].replace("^", "**"), exp[1]))
