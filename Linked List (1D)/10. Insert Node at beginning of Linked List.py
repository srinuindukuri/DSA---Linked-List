class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Insert_at_First(head, new_element):
    if head is None:
        return new_element
    newNode = Node(new_element)
    newNode.next = head
    head = newNode
    return head


def Print_LL(head):
    while(head is not None):
        print(head.data, end=" ")
        head = head.next


arr = [20, 30, 40]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])

head = Insert_at_First(head, 10)
Print_LL(head)
