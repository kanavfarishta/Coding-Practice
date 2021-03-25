# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:22:00 2021

@author: Kanav Farishta
"""

# Length of Loop in Linked List

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
            
    def loopFinder(self):
        temp = self.head
        prev= None
        rootCause = None
        while(temp):
            try:
                rootCause = temp.data[1]
                print("Loop starts from",prev.data[0])
                (prev.data).append('True')
                rootCause = temp
                break
            except:
                temp.data = [temp.data,1]
            prev= temp
            temp = temp.next
        count=0
        while(rootCause):
            count +=1
            try:
                temp = rootCause.data[2]
                print("Count is ",str(count))
                break
            except:
                rootCause = rootCause.next
            
            
LL = LinkList()

LL.append(1)
LL.append(3)
LL.append(12)
LL.append(2)
LL.append(21)
LL.append(23)
""" ======Loop Creation ======="""
node = Node(5)
inBetween = None
temp = LL.head
count= 0
while(temp.next):
    if(count==2):
        inBetween = temp
    count +=1
    temp = temp.next
temp.next = node
node.next = inBetween
#LL.traverse() #uncomment this to validate the loop
LL.loopFinder()