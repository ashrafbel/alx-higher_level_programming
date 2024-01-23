def safe_print_list(my_list=[], x=0):
    Ct = 0
    try:
        while Ct < x:
            print(my_list[Ct], end="")
            Ct += 1
    except IndexError:
        None
    print()
    return Ct
