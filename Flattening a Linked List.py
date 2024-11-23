#User function Template for python3
#Given a Linked List, where every node represents a sub-linked-list and contains two pointers:
#(i) a next pointer to the next node,
#(ii) a bottom pointer to a linked list where this node is head.
#Each of the sub-linked lists is in sorted order.
#Flatten the Link List so all the nodes appear in a single level while maintaining the sorted order.

#Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        #Your code here
        r=[]
        cur=root
        while cur:
            r.append(cur.data)
            cur2=cur.bottom
            while cur2:
                r.append(cur2.data)
                cur2=cur2.bottom
            cur=cur.next
        r.sort()
        root=Node(r[0])
        cur=root
        for i in range(1,len(r)):
            cur.bottom=Node(r[i])
            cur=cur.bottom
        return root
