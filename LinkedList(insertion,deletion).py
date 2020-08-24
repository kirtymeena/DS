# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:06:02 2020

@author: Kirty
"""

"""
LINKED LIST:
    
    COMPLEXITY:
        Insertion/Deletion : O(1)
        Access element    :  O(n)    
"""
# --------------------------------------------------------------------------------------

# class to insert data
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
    
     # function to insert the node in between
        # A -> B -> E -> C -> D
    def InBetween(self,data,node1):
        new_node = Node(data)
        cur_node  = self.head
        while cur_node.data != node1:
            cur_node = cur_node.next
        new_node.next = cur_node.next
        cur_node.next=new_node
        
        
# -----------------------------------------------------------------------------------------
    # a -> b -> c -> D 
    def delete(self,key):
        
        cur_node=self.head
        prev = None
        # list is empty(no list exist)
        if self.head is None:
            return
        
        # if first element is the key
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node = None
            return 
        # list exist and key some node
        while cur_node and cur_node.data!=key:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = cur_node.next
        cur_node=None
        
        
    def delete_at_postion(self,pos):
        
        cur_node=self.head
        if pos==0:
            self.head=cur_node.next
            return 
        
        prev=None
        count=1
        while cur_node and count!=pos:
            prev=cur_node
            cur_node=cur_node.next
            count+=1
            
            
        if cur_node is None:
            return
        prev.next=cur_node.next
        
            
        
        
            
# a -> b -> c -> d
            
            
        
                
            
        
        
    
       
            
ll=LinkedList()
ll.insert("A")
ll.insert("B")
ll.insert("C")
ll.insert("D")

# print(ll.print_list())
# print(ll.prepend("E"))

# ll.InBetween('E','B')
# ll.delete("C")
ll.delete_at_postion(2)
ll.print_list()

        
            
            
            
            
            
            
            
            
        
    

        
































