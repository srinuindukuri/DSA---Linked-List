# Insert Element Before Head of Doubly Linked List

class Node:
    def __init__(self, data, next1=None, back1=None):
        self.data = data
        self.next = next1
        self.back = back1


def ConvertArr_to_DLL(head):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    return head


def Print_DLL(head):
    while(head is not None):
        print(head.data, end=" ")
        head = head.next


def Insert_at_Head(head, k):
    newHead = Node(k, head, None)

    head.back = newHead
    return newHead


arr = [20, 30, 40]

head = ConvertArr_to_DLL(arr)
print("Original Doubly Linked List:", end=" ")
Print_DLL(head)
k = 10
print("\n\nAfter Inserting the Element:", end=" ")
head = Insert_at_Head(head, k)
Print_DLL(head)
