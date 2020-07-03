#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        if b == 0:
            result = None
        else:
            result = a / b
        print("Inside result: {}".format(result))
        return result
