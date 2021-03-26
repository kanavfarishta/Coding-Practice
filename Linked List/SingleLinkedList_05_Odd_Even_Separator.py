# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:38:23 2021

@author: Kanav Farishta
"""

#Single Linked List Reverse

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList():
    
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if(self.head==None):
            #First Insert
            newNode = Node(data)
            self.head = newNode
        else:
            #Not First Insert
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(data)
    def traverse(self):
        temp = self.head    
        while(temp):
            if(temp.next==None):
                print(temp.data)
                break
            print(temp.data,end="-->")
            temp = temp.next
    
    def separator(self):
        temp  =self.head
        LLodd = LinkList()
        LLeven = LinkList()
        while(temp):
            if(temp.data%2):
                LLeven.append(temp.data)
            else:
                LLodd.append(temp.data)
            temp = temp.next
        LLodd.traverse()
        LLeven.traverse()
        #If do not want to print 
        #return([LLodd,LLeven])

LL = LinkList()

LL.append(1)
LL.append(3)
LL.append(12)
LL.append(2)
LL.append(21)
LL.append(23)
LL.traverse()   
LL.separator()     