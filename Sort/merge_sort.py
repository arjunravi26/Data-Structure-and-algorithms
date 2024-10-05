def divide(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left, right = divide(lst[:mid]), divide(lst[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


print(divide([1, 3, 5, 2, 10, 9, 87, 6]))
