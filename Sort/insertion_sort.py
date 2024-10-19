def insertion_sort(lst):
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
print(insertion_sort(ls))
# first pass
#  [1,3],5,6,90,2
#  second pass
#  [1,3,5],6,90,2
#  third pass
# [1,3,5,6],90,2
#  fourth pass
# [1,3,5,6,90],2
# fifth pass
# [1,2,3,5,6,90]

# Insertion Sort
# Explanation:
# Insertion Sort builds a sorted array one element at a time by comparing each new element with the already sorted portion and inserting it into the correct position.
# Applications:
# Small datasets.
# Partially sorted arrays.
# Real-time systems, as it can sort during insertion.
# Advantages:
# Simple and easy to implement.
# Efficient for small and nearly sorted arrays.
# Stable sort.
# Disadvantages:
# Inefficient for large datasets.
# Time Complexity:
# Best Case: O(n) (when the array is nearly sorted)
# Average Case: O(n²)
# Worst Case: O(n²)
# Space Complexity:
# O(1) (in-place sorting)
