class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def lst_linked_list(lst):
    head = Node(lst[0])
    temp = head
    for i in lst[1:]:
        new_value = Node(i)
        temp.next = new_value
        temp = temp.next
    return head


ls = [1, 2, 4, 6, 70, 23]
head = lst_linked_list(ls)
while head:
    print(head.data)
    head = head.next