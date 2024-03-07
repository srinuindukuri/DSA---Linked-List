# You are given an array ‘Arr’ of size ‘N’ consisting of positive integers.
# Make a linked list from the array and return the head of the linked list.
# The head of the linked list is the first element of the array, and the tail of the linked list is the last element.

# ---------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructLL(arr) -> Node:
    # 'n' be the size of the array 'arr'
    n = len(arr)

    # 'head' variable stores the head of the linked list
    head = Node(arr[0])
    temp = head

    for i in range(1, n):
        # Attach current node to the "next" of the previous node
        curNode = Node(arr[i])
        temp.next = curNode
        temp = temp.next  # temp = curNode

    return head


arr = [5, 4, 3, 2]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

# Print the length of the linked list
print("Length of the linked list:", constructLL(head))
