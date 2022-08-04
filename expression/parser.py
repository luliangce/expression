import io
import re
import tokenize
from typing import List

from expression.operators import BaseOperator, get_operator, is_operator
from expression.stack import Stack
from expression.utils import is_num, is_var

all_op = {i.literal for i in BaseOperator.__subclasses__()}


def parse_token(exp: str) -> List[str]:
    tks = tokenize.tokenize(io.BytesIO(exp.encode("utf-8")).readline)
    next(tks)
    result = [tk.string for tk in tks if tk.string]

    # 矫正负数
    # tokenize会将负数解析为两个元素，实际上应该是一个
    # 当连续两个元素都不是数字时，第二个元素如果时+-，将这个符号与后一个元素合并，一起转换为浮点数
    should_combine_next = True
    i = 0
    while i < len(result):
        e = result[i]
        if re.match(r"^[\+-]+$", e) and should_combine_next:
            result[i + 1] = e + result[i + 1]
            del result[i]
            continue
        should_combine_next = is_operator(result[i])
        i += 1
    return result


def parse(exp: str) -> Stack:
    """将字符表达式解析为后置表达式的栈
    1 + 1 => 1 1 +
    1 + 1 + 1 => 1 1 + 1 +
    1 + 2 * 3 => 3 2 * 1 +
    """

    helper = []
    tokens = parse_token(exp)
    stack = Stack()
    for tk in tokens:
        if is_num(tk):
            stack.push(float(tk))
        elif is_var(tk):
            stack.push(tk)
        elif is_operator(tk):
            while True:
                op = get_operator(tk)
                if len(helper) == 0 or helper[-1] == "(":
                    helper.append(op)
                    break
                if helper[-1].priority >= op.priority:
                    stack.push(helper.pop())
                else:
                    helper.append(op)
                    break

        elif tk == "(":
            helper.append(tk)
        elif tk == ")":
            while helper[-1] != "(":
                stack.push(helper.pop())
            helper.pop()

    if helper:
        stack.push(*helper)
    return stack
