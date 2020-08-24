# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:16:54 2020

@author: Kirty
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Linked list class        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    # function to insert the elements
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    
    #function to print the list 
        # A --> B --> C --> D --> E -->none
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end=" ")
            cur_node=cur_node.next
    
    
    
    # function to prepend
            # E -> A -> B -> c -> D
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
        
        
        
        
ll=LinkedList()
ll.insert("A")
ll.insert("B")
ll.insert("C")
ll.insert("D")


print(ll.prepend("E"))


ll.print_list()
