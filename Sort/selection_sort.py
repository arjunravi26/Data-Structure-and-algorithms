def selection_sort(lst):
    if not lst:
        return None
    n = len(lst)
    for i in range(n):
        key = i
        for j in range(i+1, n):
            if lst[key] > lst[j]:
                key = j
        if key != i:
            lst[i], lst[key] = lst[key], lst[i]
    return lst


ls = [3, 1, 5, 6, 90, 2]
print(selection_sort(ls))
