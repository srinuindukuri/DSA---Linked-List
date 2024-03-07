# Problem Statement: Given the head of a linked list and an integer value,
# find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

# ----------------------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to check if a given element is present in the linked list
def check_if_present(head, value):
    temp = head

    # Traverse the linked list
    while temp is not None:
        # Check if the current node's data is equal to the desired element
        if temp.data == value:
            return 1  # Return 1 if the element is found

        # Move to the next node
        temp = temp.next

    return 0  # Return 0 if the element is not found in the linked list


# Main function
arr = [1, 2, 3]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])

value = 3  # Element to be checked for presence in the linked list

# Call the check_if_present function and print the result
print(check_if_present(head, value))
