def dsum(digit):
    if digit == 0:
        return 0
    return digit % 10 + dsum(digit//10)


print(dsum(1914))
