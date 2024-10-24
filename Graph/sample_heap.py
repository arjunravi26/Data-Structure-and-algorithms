# larges 3 elements from an unsorted array using heap

def hepify_down(arr, n, i):
    largest = i
    left_idx = (2*i) + 1
    right_idx = (2*i) + 2
    if left_idx < n and arr[left_idx] < arr[largest]:
        largest = left_idx
    if right_idx < n and arr[right_idx] < arr[largest]:
        largest = right_idx
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        hepify_down(arr, n, largest)


def heap(arr):
    n = len(arr)
    for i in range((n//2)-1,-1,-1):
        hepify_down(arr,n,i)
    largest_elements = []
    for i in range(n-1,0,-1):
        if len(largest_elements) < 3:
            arr[0],arr[i] = arr[i],arr[0]
            largest_elements.append(arr[0])
            hepify_down(arr,i,0)
        else:
            break
    return largest_elements

arr = [4,51,0,66,2,5]
print(heap(arr))
