#!/usr/bin/python3
def magic_calculation(a, b):
    R = 0
    for s in range(1, 3):
        try:
            if s > a:
                raise Exception('Too far')
            R += a ** b / i
        except Exception:
            R += b + a
            break
    return R
