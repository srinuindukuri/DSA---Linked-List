# Insert Element (Before) the End of Doubly Linked List

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


def Insert_Before_Tail(head, k):
    tail = head
    while(tail.next is not None):
        tail = tail.next

    prev = tail.back
    newNode = Node(k, tail, prev)

    tail.back = newNode
    prev.next = newNode

    return head


arr = [10, 20, 30]

head = ConvertArr_to_DLL(arr)
print("Original Doubly Linked List:", end=" ")
Print_DLL(head)

print("\n\nAfter Inserting the Element:", end=" ")
head = Insert_Before_Tail(head, 40)
Print_DLL(head)
