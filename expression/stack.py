from decimal import Decimal
from typing import List, Optional, Union

from expression.operators import BaseOperator
from expression.utils import is_num

TVar = str  # 变量

TElement = Union[BaseOperator, TVar, float, int, Decimal]


class Stack:
    _elements = None

    def __init__(self, elements: Optional[List[TElement]] = None) -> None:
        self._elements = elements or []

    def push(self, *elements: TElement) -> 'Stack':
        for e in elements:
            self._elements.append(e)
        return self

    def pop(self) -> TElement:
        return self._elements.pop()

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def __len__(self) -> int:
        return self._elements.__len__()

    def __repr__(self) -> str:
        return self._elements.__repr__()

    def calc(self) -> float:
        calc_stack = []

        for i in self._elements:
            if is_num(i):
                calc_stack.append(i)
                continue
            right, left = calc_stack.pop(), calc_stack.pop()
            calc_stack.append(i.execute(left, right))

        return calc_stack[0] if calc_stack else 0