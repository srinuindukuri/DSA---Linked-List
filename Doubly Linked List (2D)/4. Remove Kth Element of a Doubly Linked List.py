# Remove Kth Element of a Doubly Linked List

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


def Deletion_at_Head(head):
    if (head is None or head.next is None):
        return None

    prev = head
    head = head.next
    head.back = None
    prev.next = None
    return head


def Deletion_at_Tail(head):
    if(head is None or head.next is None):
        return None

    tail = head
    while(tail.next is not None):
        tail = tail.next

    newTail = tail.back
    tail.back = None
    newTail.next = None
    return head


def Print_DLL(head):
    while(head is not None):
        print(head.data, end=" ")
        head = head.next


def RemoveKthElement(head, k):
    if (head is None):
        return None

    cnt = 0
    KNode = head
    while(KNode is not None):
        cnt += 1
        break
    KNode = KNode.next

    prev = KNode.back
    front = KNode.next

    if(prev is None and front is None):
        return None
    elif (prev is None):
        return Deletion_at_Head(head)
    elif (front is None):
        return Deletion_at_Tail(head)

    prev.next = front
    front.back = prev

    KNode.next = None
    KNode.back = None
    return head


arr = [12, 5, 8, 7]

head = ConvertArr_to_DLL(arr)
print("Original Doubly Linked List:", end=" ")
Print_DLL(head)

print("\n\nAfter deleting the head node:", end=" ")
head = RemoveKthElement(head, 2)
Print_DLL(head)
