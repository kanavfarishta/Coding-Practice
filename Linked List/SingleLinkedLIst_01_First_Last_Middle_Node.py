# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:37:23 2021

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
    
    def nthNode(self,nth):
        temp = self.head
        count =0
        flag = True
        while(temp):
            count+=1
            if(count==nth):
                return(temp.data)
            temp = temp.next
        if(flag):
            raise Exception("{} Node does not exisit".format(str(nth)))

    def nthNodeFromEnd(self,nth):
        temp = self.head
        length =0
        while(temp):
            length+=1
            temp = temp.next
        value = length-nth
        if(value>length or value <0):
            raise Exception("{} Node does not exisit".format(str(nth)))
        length =0 
        temp = self.head
        while(temp):
            length+=1
            if(length==value):
                return(temp.data)
            temp = temp.next
    def middle(self):
        length = 0
        temp = self.head
        while(temp):
            length +=1
            temp = temp.next
        if(length ==0 or length==1):
            raise Exception("Middle is not possible")
        mid = length/2
        self.printValue(self.head,mid,True if length%2==0 else False)
    
    def printValue(self,temp,value,flag):
        count= 0
        while(temp):
            count+=1
            if(count==value):
                print(temp.data,temp.next.data if flag else "")
            temp = temp.next
            
            
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

print(LL.nthNode(3))
print(LL.nthNodeFromEnd(2))
LL.middle()