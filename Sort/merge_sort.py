def divide(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left, right = divide(lst[:mid]), divide(lst[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


print(divide([1, 3, 5, 2, 10, 9, 87, 6]))

# 5. Merge Sort
# Explanation:
# Merge Sort is a divide-and-conquer algorithm that splits the array into two halves, recursively sorts them, and then merges the two sorted halves.
# Applications:
# Linked lists (works well with linked data structures).
# External sorting (where data is too large to fit into memory).
# Stable sort required, such as in merge-based search algorithms.
# Advantages:
# Efficient on large datasets.
# Stable sort.
# Guaranteed O(n log n) performance.
# Disadvantages:
# Requires additional memory (space complexity of O(n)).
# Not in-place, making it less efficient for memory-constrained environments.
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)
# Space Complexity:
# O(n) (due to extra arrays used in the merging process)
