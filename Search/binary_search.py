class BinarySearch:
    def __init__(self, data) -> None:
        self.data = sorted(data)

    def find(self, element):
        low = 0
        high = len(self.data) - 1
        while low <= high:
            mid = (low+high) // 2
            if self.data[mid] == element:
                return mid
            elif self.data[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return -1


lst = [1, 4, 56, 73, 3, 0]
binary_search = BinarySearch(lst)
pos = binary_search.find(56) # This will print the index of the element '56' in the sorted list

print(pos)