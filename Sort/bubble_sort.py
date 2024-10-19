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
#  Last element will get correct position
# eg: first pass:
#  [1,3,5,6,2,90] greatest element comes last
#  second pass
#  [1,3,5,2,6,90] second greatest element comes second last
# third pass
#  [1,3,2,5,6,90] third greatest element comes third last and so on

# Bubble Sort
# Explanation:
# Bubble Sort compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the array is sorted.
# Applications:
# Simple cases where the array is nearly sorted or small.
# Educational purposes to understand basic sorting algorithms.
# Advantages:
# Simple to understand and implement.
# In-place sorting (no extra space required).
# Stable sort (preserves relative order of equal elements).
# Disadvantages:
# Very inefficient for large arrays.
# Requires multiple passes even for a nearly sorted array.
# Time Complexity:
# Best Case: O(n) (if the array is already sorted)
# Average Case: O(n²)
# Worst Case: O(n²)
# Space Complexity:
# O(1) (in-place sorting)
