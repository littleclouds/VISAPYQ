''' Given a singly linked list. The task is to remove duplicates (nodes with duplicate values) from the given list (if it exists). '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        # If the list is empty or has only one node, return the head
        if head is None or head.next is None:
            return head

        # Initialize current node
        current = head

        # Traverse the list
        while current is not None and current.next is not None:
            # If current node's data is equal to next node's data
            if current.data == current.next.data:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Creating a linked list with duplicates
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(3)

    print("Original list:")
    printList(head)

    solution = Solution()
    head = solution.removeDuplicates(head)

    print("List after removing duplicates:")
    printList(head)
