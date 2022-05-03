def max_integer(my_list=[]):

    largest_number = my_list[0]
    lens = len(my_list)
    for number in my_list:
        if lens <= 0:
            return(None)
        elif number > largest_number:
            largest_number = number
            return(largest_number)
