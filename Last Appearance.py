'''You are given an unsorted Singly Linked List with 'N' nodes which may contain duplicate elements. You are supposed to remove all duplicate elements from the linked list and keep only the last appearance of elements.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        if not head:
            return None

        current = head
        prev = None
        seen = {}

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen[current.data] = current
                prev = current
            current = current.next

        return head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")

# Example usage
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(3)

    print("Original list:")
    printList(head)

    solution = Solution()
    head = solution.removeDuplicates(head)

    print("List after removing duplicates:")
    printList(head)
