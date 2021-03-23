# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:24:21 2021

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
    def search(self,data):
        temp = self.head
        flag = True
        while(temp):
            if(temp.data==data):
                flag = False
                return("Found the Value")
            temp = temp.next
        if(flag):
            return("No such Value")
    
    def searchRecursive(self,data):
        temp = self.head
        return(self.recursive(temp,data))
    
    def recursive(self,temp,data):
        if(temp==None):
            return("No such Value")
        elif(temp.data == data):
            return("Found the Value")
        else:
            return(self.recursive(temp.next,data))
    def count(self,data):
        temp = self.head
        count = 0
        while(temp):
            if(data==temp.data):
                count +=1
            temp = temp.next
        return(count)
    def countRecursive(self,data):
        temp = self.head
        count=0
        return(self.recursive1(temp,count,data))
    def recursive1(self,temp,count,data):
        if(temp==None):
            return(count)
        elif(temp.data==data):
            return(self.recursive1(temp.next,count+1,data))
        else:
            return(self.recursive1(temp.next,count,data))
LL = LinkList()

LL.append(1)
LL.append(3)
LL.append(12)
LL.append(2)
LL.append(4)
LL.append(17)
LL.append(1)
LL.append(3)
LL.traverse()
print(LL.search(4))
print(LL.searchRecursive(4))

print(LL.count(41))
print(LL.countRecursive(42))

print(LL.count(1))
print(LL.countRecursive(3))