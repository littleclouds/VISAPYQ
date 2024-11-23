#User function Template for python3


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