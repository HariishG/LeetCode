class MyLinkedList:
    class Node:
        def __init__(self, val=None, next=None):
            self.val=val
            self.next=next

    def __init__(self):
        self.length=0
        self.head=None

    def get(self, index: int) -> int:
        if index<self.length:
            temp=self.head
            for i in range(index):
                temp=temp.next
            if temp.val==-1:
                return -1
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.head=self.Node(val, self.head)
        self.length+=1
    def addAtTail(self, val: int) -> None:
        if self.head==None:
            self.head=self.Node(val)
            self.length+=1
            return
        temp=self.head
        for i in range(self.length-1):
            temp=temp.next
        temp.next=self.Node(val)
        self.length+=1
        self.printNode()
    def addAtIndex(self, index: int, val: int) -> None:
        if self.head==None and index==0:
            self.head=self.Node(val)
            self.length+=1
            return
        if index==0:
            self.addAtHead(val)
            return
        if index==self.length:
            self.addAtTail(val)
            return
        if index<=self.length:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=self.Node(val,temp.next)
            self.length+=1
        # else:
        #     self.head=self.Node(-1)
        #     curr=self.head
        #     self.length=1
        #     for i in range(index-self.length):
        #         # print(i)
        #         curr.next=self.Node(-1)
        #         curr=curr.next
        #         self.length+=1
        #     curr.next=self.Node(val)
        #     self.length+=1
        #     self.printNode()

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index<self.length:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            if temp.next and temp.next.next:
                temp.next=temp.next.next
            else:
                temp.next=None
            self.length-=1
        return
    def printNode(self):
        curr=self.head
        print(curr.val, end=' ')
        while curr.next:
            print(curr.next.val, end= ' ')
            curr=curr.next
        print()