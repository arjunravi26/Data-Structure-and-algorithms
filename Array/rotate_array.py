lst = [1, 2, 3, 4, 6, 8, 9]
k = 2
print(lst)
for _ in range(k):
    lst.insert(0,lst.pop())
print(lst)
