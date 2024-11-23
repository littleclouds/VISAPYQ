'''Design a data structure that works like a LRU Cache. Here cap denotes the capacity of the cache and Q denotes the number of queries. Query can be of two types:

SET x y: sets the value of the key x with value y
GET x: gets the key of x if present else returns -1.
The LRUCache class has two methods get() and set() which are defined as follows.

get(key): returns the value of the key if it already exists in the cache otherwise returns -1.
set(key, value): if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.
In the constructor of the class the capacity of the cache should be initialized.
'''

#Back-end complete function Template for Python 3

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None

class LRUCache:
    hsmap=dict()
    capacity=count=0
    head=tail=None
    
    #Constructor for initializing the cache capacity with the given value.
    def __init__(self,cap):
        self.hsmap=dict()
        self.capacity=cap
        self.head=Node(0,0)
        self.tail=Node(0,0)
        
        self.head.next=self.tail
        self.head.pre=None
        self.tail.next=None
        self.tail.pre=self.head
        count=0
        
    def addToHead(self,node):
        node.next=self.head.next
        node.next.pre=node
        node.pre=self.head
        self.head.next=node
    
    #Function to delete a node.
    def deleteNode(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre
    
    #Function to return value corresponding to the key.
    def get(self,key):
        
        #if element is present in map,
        if key in self.hsmap:
            
            node=self.hsmap[key]
            result=node.value
            self.deleteNode(node)
            self.addToHead(node)
            
            #returning the value.
            return result
         
        #else we return -1.   
        else:
            return -1
        
    #Function for storing key-value pair.   
    def set(self,key,value):
        
        if key in self.hsmap:
            
            node=self.hsmap[key]
            node.value=value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node=Node(key,value)
            self.hsmap[key]=node
            
            if self.count<self.capacity:
                self.count+=1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.pre.key)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)
