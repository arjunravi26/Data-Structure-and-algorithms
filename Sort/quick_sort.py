def quick(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    print(pivot)
    right = []
    left = []
    pivot_val = []
    for i in lst:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            pivot_val.append(i)  # handle duplicate values also
    return quick(left) + pivot_val + quick(right)


print(quick([1, 3, 4, 4, 2, 0]))
