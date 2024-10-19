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



# Explanation:
# Quick Sort is a divide-and-conquer algorithm that selects a "pivot" element and partitions the array into two halves: elements less than the pivot on one side, and elements greater than the pivot on the other. It then recursively sorts the sub-arrays.
# Applications:
# Large datasets.
# Systems with limited memory since it can be in-place.
# General-purpose sorting in real-world applications.
# Advantages:
# Efficient on large datasets.
# In-place sorting (when implemented properly).
# Divide-and-conquer strategy works well with modern CPU architectures.
# Disadvantages:
# Unstable sorting algorithm.
# Worst-case time complexity is O(n²) if pivot selection is poor.
# Recursive, which could lead to a stack overflow on large datasets if not optimized with tail recursion or using iterative approaches.
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²) (if pivot selection is poor)
# Space Complexity:
# O(log n) (due to recursion in the best case)
# O(n) (in the worst case, due to stack depth)
