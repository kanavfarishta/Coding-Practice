# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:50:33 2021

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
    def deleteFirst(self):
        if(self.head==None):
            raise Exception("Nothing to Delete")
        self.head = self.head.next
    def deleteLast(self):
        if(self.head==None):
            raise Exception("Nothing to Delete")
        else:
            temp = self.head
            prev = None
            while(temp.next):
                prev = temp
                temp = temp.next
            prev.next = None
    def delete(self,data):
        if(self.head==None):
            raise Exception("Nothing to Delete")
        else:
            temp = self.head
            prev = None
            flag = True
            while(temp):
                if(data==temp.data):
                    flag = False
                    if(prev==None):
                        self.head = temp.next
                    else:
                        prev.next = temp.next
                prev= temp    
                temp = temp.next
            if(flag):
                raise Exception("Nothing to delete")
    def deleteAfter(self,data):
        if(self.head==None):
            raise Exception("Nothing to Delete")
        else:
            temp = self.head
            flag = True
            while(temp):
                if(data == temp.data):
                    if(temp.next==None):
                        break
                    temp.next = temp.next.next
                    flag = False
                    break
                temp = temp.next
            if(flag):
                raise Exception("Nothing to Delete")
                    
    def deleteBefore(self,data):
        if(self.head==None):
            raise Exception("Nothing to Delete")
        else:
            temp = self.head
            prev = None
            prePrev = None
            flag = True
            while(temp):
                if(data==temp.data):
                    flag = False
                    if(prev==None):
                        raise Exception("Nothing to Delete")
                    if(prePrev == None):
                        self.head = temp
                        break
                    else:
                        prePrev.next = temp
                        break
                prePrev = prev
                prev = temp
                temp = temp.next
            if(flag):
                raise Exception("Nothing to Delete")
       

"""====== Invoking ======="""

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
LL.deleteFirst()
LL.deleteLast()
LL.traverse()
LL.deleteBefore(18)
LL.deleteAfter(2)
LL.delete(2)
LL.traverse()