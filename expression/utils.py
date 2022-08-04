def is_num(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False
