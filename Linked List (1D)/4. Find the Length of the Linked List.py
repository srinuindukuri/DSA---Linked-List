# Given the head of a singly linked list of integers, find and return its length.

# Sample Input 1 :
# 3 4 5 2 6 1 9 - 1

# Sample Output 1:
# 7

# Explanation of sample input 1:
# The number of nodes in the given linked list is 7.

# Hence we return 7.
# ------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LengthofLL(head):
    count = 0
    temp = head

    while(temp != None):
        temp = temp.next
        count += 1
    return count


# Main Function
arr = [2, 5, 8, 7, 12]
# Create a linked list
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Print the length of the linked list
head = LengthofLL(head)
print(head)
