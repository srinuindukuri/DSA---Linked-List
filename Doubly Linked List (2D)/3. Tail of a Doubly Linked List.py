# Delete Last Node of a Doubly Linked List

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


def Delete_Tail(head):
    if(head is None or head.next is None):
        return None

    tail = head
    while(tail.next is not None):
        tail = tail.next

    newTail = tail.back
    tail.back = None
    newTail.next = None
    return head


arr = [12, 5, 7, 8]

head = ConvertArr_to_DLL(arr)
print("Linked List Before Deleting Tail..", end=" ")
Print_DLL(head)

head = Delete_Tail(head)
print("\n\nLinked List After Deleting Tail..", end=" ")
Print_DLL(head)
