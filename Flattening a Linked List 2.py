''' Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.
'''

#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def mergeTwoLists(a, b):
    """Helper function to merge two sorted linked lists"""
    if not a:  # If list 'a' is empty
        return b
    if not b:  # If list 'b' is empty
        return a
    
    # Compare and merge
    if a.data < b.data:
        result = a
        result.bottom = mergeTwoLists(a.bottom, b)
    else:
        result = b
        result.bottom = mergeTwoLists(a, b.bottom)
    
    return result

def flattenLinkedList(root):
    if not root or not root.next:
        return root
        
        # Recursively flatten the next linked list
    root.next = flattenLinkedList(root.next)
        
        # Merge the current list with the flattened next list
    root = mergeTwoLists(root, root.next)
        
    return root
    
    
class Solution():
    
    def flatten(self,root):
        #Your code here
        return flattenLinkedList(root)
        
                    
