from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from typing import Optional


class BaseOperator(ABC):

    @abstractproperty
    def priority(self) -> int:
        """运算符优先级"""
        pass

    @abstractproperty
    def literal(self) -> str:
        """字面量，如Add的字面量就是+"""
        pass

    @staticmethod
    @abstractmethod
    def execute(left: float, right: float) -> float:
        pass

    def __repr__(self) -> str:
        return self.literal

    __str__ = __repr__


def inner_meta(repr: str = ""):

    class Inner(ABCMeta):

        def __new__(cls, name, bases, attrs):
            cls.__name__ = "123"

            return super().__new__(cls, name, bases, attrs)

        def __repr__(self) -> str:
            return repr

        def __str__(self) -> str:
            return repr

    return Inner


def quick_define(literal: str, func, p: int = 1) -> BaseOperator:
    _literal = literal  # avoid name conflict

    class Operator(BaseOperator, metaclass=inner_meta("{}".format(literal))):
        literal = _literal
        priority = p

        @staticmethod
        def execute(left: float, right: float) -> float:
            return func(left, right)

    return Operator


Add = quick_define('+', lambda left, right: left + right)
Minus = quick_define('-', lambda left, right: left - right)
Mul = quick_define('*', lambda left, right: left * right, p=2)
Div = quick_define('/', lambda left, right: left / right, p=2)
Mod = quick_define("%", lambda left, right: left % right, p=2)
Pow = quick_define("^", lambda left, right: left**right, p=3)
Pow2 = quick_define("**", lambda left, right: left**right, p=3)


def get_operator(op: str, safe=True) -> Optional[BaseOperator]:
    for i in BaseOperator.__subclasses__():
        if i.literal == op:
            return i
    if safe:
        return None
    raise ValueError("Unknown operator: {}".format(op))


def is_operator(op: str):
    return get_operator(op) is not None


if __name__ == "__main__":
    print(Add().execute(1, 2))
    print(Minus().execute(1, 2))
    print(Mul().execute(1, 2))
    print(Div().execute(1, 2))
