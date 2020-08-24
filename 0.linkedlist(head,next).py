# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:26:42 2020

@author: Kirty
"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__ (self):
        self.head=None
        
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
ll=linkedlist()
ll.insert("A")
ll.insert("B")

print(ll.head)
print(ll.head.data)
print(ll.head.next.data)

