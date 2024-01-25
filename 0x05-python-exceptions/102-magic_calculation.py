def magic_calculation(a, b):
    R = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            R += (a ** b) / i
        except:
            R += a + b
            break
    return R
