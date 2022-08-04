from expression.operators import is_operator


def is_num(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


def is_var(s: str):
    if not isinstance(s, str):
        return False
    if is_operator(s):
        return False
    return s.isalpha()
