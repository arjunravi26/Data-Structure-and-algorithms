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

# first pass
# [1], 2,5,6,90,2
# second pass
# [1,2], 3,5,6,90
# third pass
# [1,2,3],5, 6,90
# find the remaining smallest element from the remaining array and append it the sorted array
# Explanation:
# Selection Sort repeatedly selects the smallest (or largest) element from the unsorted portion of the array and swaps it with the first unsorted element.
# Applications:
# Small datasets.
# When memory space is limited, as it's an in-place algorithm.
# Advantages:
# Simple and easy to understand.
# Performs well on small datasets.
# In-place sorting (does not require extra space).
# Disadvantages:
# Not stable (may change the relative order of equal elements).
# Inefficient for large datasets.
# Time Complexity:
# Best Case: O(n²)
# Average Case: O(n²)
# Worst Case: O(n²)
# Space Complexity:
# O(1) (in-place sorting)
# 4. Quick Sort
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
# Summary of Time and Space Complexities:
# Algorithm	Best Time	Average Time	Worst Time	Space	Stability
# Bubble Sort	O(n)	O(n²)	O(n²)	O(1)	Yes
# Insertion Sort	O(n)	O(n²)	O(n²)	O(1)	Yes
# Selection Sort	O(n²)	O(n²)	O(n²)	O(1)	No
# Quick Sort	O(n log n)	O(n log n)	O(n²)	O(log n)	No
# Merge Sort	O(n log n)	O(n log n)	O(n log n)	O(n)	Yes
# Applications of Sorting Algorithms:
# Bubble Sort: Used in simple applications where the input is small or nearly sorted.
# Insertion Sort: Commonly used in situations where the dataset is nearly sorted or when working with online algorithms (e.g., sorting cards in a card game).
# Selection Sort: Useful when space is at a premium, though inefficient for large datasets.
# Quick Sort: Used in many systems, including the C++ STL’s sort() function and Python’s sorted(). Best for large datasets where space is limited.
# Merge Sort: Used in external sorting (e.g., large-scale data that cannot be stored in memory at once) and when stable sorting is necessary.
