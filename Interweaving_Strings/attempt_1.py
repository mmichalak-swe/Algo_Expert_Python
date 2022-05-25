def interweavingStrings(one, two, three):
    ptr_one = 0
    ptr_two = 0
    last = None
    stop = False

    for i, char_three in enumerate(three):
        if ptr_one == len(one):
            ptr_one = len(one) - 1
        if ptr_two == len(two):
            ptr_two = len(two) - 1

        ptr_one, ptr_two, last, stop = finder(one[ptr_one], ptr_one, two[ptr_two], ptr_two, char_three, i, last, stop)
        if stop is True:
            return False
        else:
            continue

    if ptr_one != len(one) and ptr_two != len(two):
        return False
    return True


def finder(char_one, ptr_one, char_two, ptr_two, char_three, i, last, stop):
    if last is None or last == "one":
        if char_one == char_three:
            ptr_one += 1
            return ptr_one, ptr_two, "one", False
        elif char_two == char_three:
            ptr_two += 1
            return ptr_one, ptr_two, "two", False
        else:
            return ptr_one, ptr_two, last, True
    else:
        if char_two == char_three:
            ptr_two += 1
            return ptr_one, ptr_two, "two", False
        elif char_one == char_three:
            ptr_one += 1
            return ptr_one, ptr_two, "one", False
        else:
            return ptr_one, ptr_two, last, True

