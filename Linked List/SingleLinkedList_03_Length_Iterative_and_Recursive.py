# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:05:58 2021

@author: Kanav Farishta
"""
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
    
    def findLength(self):
        temp = self.head
        count =0
        while(temp):
            count +=1
            temp = temp.next
        return(count)
    
    def findLengthRecursive(self):
        count = 0
        temp = self.head
        return(self.recursive(count,temp))
        
    def recursive(self,count,temp):
        if(temp==None):
            return(count)
        else:
            return(self.recursive(count+1,temp.next))
LL = LinkList()

LL.append(1)
LL.append(3)
LL.append(12)
LL.append(2)
LL.append(4)
LL.append(17)
LL.append(18)
LL.append(34)
LL.traverse()
print(LL.findLength())
print(LL.findLengthRecursive())