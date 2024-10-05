def bubble_sort(lst):
    if not lst:
        return None
    length = len(lst)
    for i in range(length):
        swapped = False
        ran = length-i-1
        for j in range(0, ran):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

ls = [3, 1, 5, 6, 90, 2]
print(bubble_sort(ls))
