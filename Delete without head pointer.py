"""
You are given a node del_node of a Singly Linked List where you have to delete a value of the given node from the linked list but you are not given the head of the list.
By deleting the node value, we do not mean removing it from memory. We mean:
The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before & after the del_node node should be in the same order.
Constraints:
2 <= number of nodes <= 106  
1 <= node->data <= 106 
"""
'''
    Your task is to delete the given node from
    the linked list, without using head pointer.
    
    Function Arguments: node (given node to be deleted) 
    Return Type: None, just delete the given node from the linked list.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
class Solution:
    # Function to delete a node in the middle of a singly linked list.
    def deleteNode(self, node):
        #code here
        if node is None or node.next is None:
            return
        node.data=node.next.data
        node.next=node.next.next
