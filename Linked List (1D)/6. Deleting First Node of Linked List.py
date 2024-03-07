class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Delete_Head(head):
    if head is None:
        return head
    return head.next


def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


arr = [1, 2, 3]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head = Delete_Head(head)
print_ll(head)
