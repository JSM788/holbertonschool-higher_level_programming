def max_integer(my_list=[]):

    new_list = sorted(my_list)
    lens = len(new_list)
    if lens == 0:
        return(None)
    else:
        return(new_list[-1])
