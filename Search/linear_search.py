class LinearSearch:
    def __init__(self, data) -> None:
        self.data = data

    def find(self, element):
        for index, val in enumerate(self.data):
            if val == element:
                return index
        return -1


lst = [1, 2, 4, 7, 8, 0]
linear_seach = LinearSearch(lst)
pos = linear_seach.find(48)
print(pos)
