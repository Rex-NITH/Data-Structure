class node:
    def __init__(self,val):
        self.data=val
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insertAtHead(self,val):
        newnode=node(val)
        if (self.head==None):
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.size+=1

    def insertAtTail(self,val):
        newnode=node(val)

        if (self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
        self.size+=1

    def insertAtPos(self,val,pos):
        newnode=node(val)
        if (pos==0):
            self.insertAtHead(val)
        elif (pos==self.size):
            self.insertAtTail(val)
        elif(pos<self.size):
            index=0
            temp=self.head
            while(index!=pos-1):
                temp=temp.next
                index+=1
            newnode.next=temp.next
            temp.next=newnode
        else:
            print("position is out of index")

    def deleteAtTail(self):
        if (self.head==None):
            print("list is empty")
        else:
            temp=self.head
            while(temp.next.next is not None):
                temp=temp.next
            temp.next=None

    def deleteAtHead(self):
        if (self.head==None):
            print("list is empty")
        else:
            self.head=self.head.next

    def deleteAtPos(self,pos):
        if (pos==0):
            self.deleteAtHead
        elif(pos==self.size):
            self.deleteAtTail
        elif(pos<self.size):
            index=0
            temp=self.head
            while(index!=pos-1):
                temp=temp.next
                index+=1
            temp.next=temp.next.next
            
        else:
            print("position excide the length")

        
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,"->",end="")
            temp=temp.next
        print("None")
        
if __name__=="__main__":
    ll=LinkedList()
    ll.insertAtHead(2)
    ll.insertAtHead(1)
    ll.insertAtTail(3)
    ll.insertAtPos(0,0)
    ll.display()
    ll.deleteAtTail()
    ll.display()
    ll.deleteAtHead()
    ll.display()
    ll.deleteAtPos(1)
    ll.display()
