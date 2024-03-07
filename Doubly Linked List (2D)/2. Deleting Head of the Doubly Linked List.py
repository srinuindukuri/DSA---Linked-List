class Node:
    def __init__(self, data, next1=None, back1=None):
        self.data = data
        self.next = next1
        self.back = back1


def convert_arr_to_dll(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head


def Deletion_at_Head(head):
    if (head is None or head.next is None):
        return None

    prev = head
    head = head.next
    head.back = None
    prev.next = None
    return head


def Print_DLL(head):
    while(head is not None):
        print(head.data, end=" ")
        head = head.next


arr = [12, 5, 8, 7]

head = convert_arr_to_dll(arr)
print("Original Doubly Linked List:", end=" ")
Print_DLL(head)

print("\n\nAfter deleting the head node:", end=" ")
head = Deletion_at_Head(head)
Print_DLL(head)
