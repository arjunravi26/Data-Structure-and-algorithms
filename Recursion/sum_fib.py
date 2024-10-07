def fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return fib(num-1) + fib(num-2)


print(fib(5))


def sum_fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return sum_fib(num-1) + fib(num)


print(sum_fib(6))
