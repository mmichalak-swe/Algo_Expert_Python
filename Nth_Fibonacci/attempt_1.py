def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n1_fib = 1
        n2_fib = 0
        counter = 3

        while counter <= n:
            curr_fib = n1_fib + n2_fib
            n2_fib = n1_fib
            n1_fib = curr_fib
            counter += 1

    return curr_fib

