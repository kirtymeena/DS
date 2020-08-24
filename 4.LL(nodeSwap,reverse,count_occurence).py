# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:36:38 2020

@author: Kirty
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
      
class LinkedList:
    def __init__(self):
        self.head = None
        
        
  
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data,end=" ")
            cur_node=cur_node.next
            
    def swap(self,node1,node2):
        cur_node1= self.head
        cur_node2 = self.head
        prev1=None
        prev2=None
        
        if node1 == node2:
            return
        
        while cur_node1 and cur_node1.data!=node1:
            prev1=cur_node1
            cur_node1=cur_node1.next
        
        while cur_node2  and  cur_node2.data!=node2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        
        
            
            
            
            
ll=LinkedList()
ll.insert("A")
ll.insert("B")
ll.insert("C")
ll.insert("D")
            