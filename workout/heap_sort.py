def heapify_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify_down(arr, n, largest)


def heapsort(arr):
    for i in range((len(arr)-1)//2, -1, -1):
        heapify_down(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, i, 0)


arr = [4, 5, 1, 9, 11, 10, 2]
heapsort(arr)
print(arr)
