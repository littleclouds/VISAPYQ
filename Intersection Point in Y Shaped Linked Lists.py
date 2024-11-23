''' Given two singly linked lists, write a program to get the point where two linked lists intersect each other. 
If the linked list does not merge at any point, it should return -1. '''

#User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.
    
    Function Arguments: head1, head2 (heads of both the lists)
    
    Return Type: Node # driver code will print the Node->data
'''
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find intersection point in Y shaped Linked Lists.
class Solution:
    def intersectPoint(self, head1, head2):
        if not head1 or not head2:
            return None
        ptr1=head1
        ptr2=head2
        while(ptr1!=ptr2):
            ptr1=ptr1.next if ptr1 else head2
            ptr2=ptr2.next if ptr2 else head1
        return ptr1
        # code here
