# O(n) time | O(1) space

def getNthFib(n):
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n1_fib = 1
        n2_fib = 0

        for i in range(2, n):
            curr_fib = n1_fib + n2_fib
            n2_fib = n1_fib
            n1_fib = curr_fib

    return curr_fib

