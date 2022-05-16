#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[0:x]:
            if type(i) == int:
                count += 1
                print("{:d}".format(i), end="")
    except Exception:
        pass
    print()
    return count
