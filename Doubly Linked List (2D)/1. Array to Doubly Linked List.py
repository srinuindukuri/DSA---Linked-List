class Node:
    def __init__(self, data, next1=None, back1=None):
        self.data = data
        self.next = next1
        self.back = back1


def Convert_DLL(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'Prev' to the Node
    prev = head
    for i in range(1, len(arr)):
        # Create a new node with data from the array and set 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp
    return head


def Print_LL(head):
    while(head is not None):
        print(head.data, end=" ")
        head = head.next


arr = [12, 5, 8, 16]
head = Convert_DLL(arr)
Print_LL(head)
