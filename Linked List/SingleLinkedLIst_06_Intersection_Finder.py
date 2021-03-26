# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:02:52 2021

@author: Kanav Farishta
"""
import random 

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
    
def intersectionFinder(head1,head2):
        temp = head1
        
        while(temp):
            temp.data =  [temp.data,1]
            temp= temp.next
        
        temp = head2
        
        while(temp):
            try:
                temp.data[1]
                print("The Intersection is at",temp.data[0])
                break
            except:
                temp = temp.next
LL = LinkList()

LL.append(1)
LL.append(3)
LL.append(12)
LL.append(2)
LL.append(21)
LL.append(23)


temp = LL.head
for i in range(0,random.randint(1,5)):
    temp = temp.next

LL1 = LinkList()
LL1.append(4)
LL1.append(6)
temp1 = LL1.head

while(temp1.next):
    temp1 = temp1.next
temp1.next = temp

LL.traverse()
LL1.traverse()

intersectionFinder(LL.head,LL1.head)