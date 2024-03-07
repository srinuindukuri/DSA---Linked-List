class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Remove_kth(head, k):
    if(head is None):
        return head
    if(k == 1):
        return head.next

    cnt = 0
    temp = head
    prev = None
    while(temp != None):
        cnt += 1
        if (cnt == k):
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head


def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


arr = [2, 5, 8, 7, 12]
# Create a linked list
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Element to be checked for presence in the linked list

head = Remove_kth(head, 2)

# Print the modified linked list
print_ll(head)
