# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:38:12 2021

@author: Kanav Farishta
"""
"""====== Single Linked List ======="""
#Linked List Insertion

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
    def pushFirst(self,data):
        if(self.head==None):
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
    def addBefore(self,data,iData):
        if(self.head==None):
            #Meaning no data
            raise Exception("No data present in the List")
        else:
            temp = self.head
            prev = None
            flag = False
            while(temp):
                if(temp.data==data):
                    flag = True
                    if(prev == None):
                        #Meaning 1st Data itself
                        self.pushFirst(iData)
                    else:
                        newNode = Node(iData)
                        prev.next = newNode
                        newNode.next = temp
                prev = temp
                temp = temp.next
            if(not flag):
                raise Exception("No data present in the List")
    def addAfter(self,data,iData):
        if(self.head==None):
            #Meaning no data
            raise Exception("No data present in the List")
        else:
            temp = self.head
            flag = False
            while(temp):
                if(temp.data==data):
                    flag = True
                    newNode = Node(iData)
                    newNode.next = temp.next
                    temp.next = newNode
                temp = temp.next
            if(not flag):
                raise Exception("No data present in the List")
    def traverse(self):
        temp = self.head
        
        while(temp):
            if(temp.next==None):
                print(temp.data)
                break
            print(temp.data,end="-->")
            temp = temp.next
        

"""====== Invoking ======="""

LL = LinkList()
#LL.addAfter(10,17)
LL.append(1)
LL.append(3)
LL.append(12)
LL.pushFirst(10)
LL.pushFirst(2)
LL.append(19)
LL.addAfter(12,17)
LL.addBefore(19,20)
LL.traverse()
          
        