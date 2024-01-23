#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []

    for v in range(list_length):
        try:
            resultofdivi = my_list_1[v] / my_list_2[v]
            nlist.append(resultofdivi)
        except ZeroDivisionError:
            print("division by 0")
            nlist.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            nlist.append(0)
        except IndexError:
            print("out of range")
            nlist.append(0)
        finally:
            pass

    return nlist
