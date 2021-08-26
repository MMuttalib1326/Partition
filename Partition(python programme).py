# Write code to partition a linked list around a value x,
# such that all node less than x come bbefore all nodes greater than or equall to x.
# python programming
from random import randint
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self,values=None):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    def __str__(self):
        value=[str(x.value) for x in self]
        return '->'.join(value)

    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result

    def add(self,value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode         
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail
    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
    def partition(ll,n):
        curnode=ll.head
        ll.tail=ll.head
        while curnode:
            nextcurnode=curnode.next
            curnode.next=None
            if curnode.value < n:
                curnode.next=ll.head
                ll.head=curnode
            else:
                ll.head.next=curnode
                ll.tail=curnode
            curnode=nextcurnode
        if ll.tail.next is not None:
            ll.tail.next=None              

customll=Linkedlist()
customll.generate(10, 0, 99)
print(customll)
customll.partition(40)  
print(customll)                       