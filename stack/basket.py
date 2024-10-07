class Solution:
    def calPoints(self, operations) -> int:
        lst = []
        for value in operations:
            print(value,len(lst))
            n = len(lst)
            if value == "+" and n >= 2:
                add = int(lst[n - 1]) + int(lst[n - 2])
                lst.append(add)
            elif value == "D" and n >= 1:
                prod = int(lst[n - 1]) * 2
                lst.append(prod)
            elif value == "C":
                lst.pop()
            elif int(value):
                lst.append(int(value))
            print(lst)
        return sum(lst)


sol = Solution()
op = ["5","-2","4","C","D","9","+","+"]
value = sol.calPoints(op)
print(value)
