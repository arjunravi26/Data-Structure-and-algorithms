def selection_sort(lst):
    if not lst:
        return None
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            print(j, key, lst[j])
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j -= 1
    return lst


ls = [3, 1, 5, 6, 90, 2]
print(selection_sort(ls))
