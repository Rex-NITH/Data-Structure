from dataclasses import dataclass


class node:
    def __init__ (self,val):
        self.data = val
        self.left = None
        self.right = None

class doublyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtHead(self,val):
        newnode = node(val)

        if (self.head==None):
            self.head = newnode
            self.size+=1
        else:
            newnode.right = self.head
            self.head.left = newnode
            self.head = newnode
            self.size+=1

    def insertAtTail(self,val):
        newnode = node(val)

        if (self.head == None):
            self.head = newnode
            self.size+=1
        else:
            temp = self.head
            while(temp.right is not None):
                temp = temp.right
            temp.right = newnode
            newnode.left = temp
            self.size+=1
    
    def deleteAtHead(self):
        if (self.head == None):
            return ("The doubly Linked List is empty")
        elif (self.head.right is None):
            self.head = None
            return
        else:
            self.head = self.head.right
            self.head.left = None

    def deleteAtTail(self):
        if (self.head == None):
            return ("The doubly Linked List is empty")
        else:
            temp = self.head

            while(temp.right.right is not None):
                temp = temp.right
            temp.right = None

    def display(self):
        if (self.head == None):
            return ("The doubly Linked List is empty")
        else:
            temp = self.head
            while(temp is not None):
                print(temp.data,"<->",end="")
                temp = temp.right
            print("None")

if __name__=="__main__":
    ll=doublyLinkedList()
    ll.insertAtHead(2)
    ll.insertAtHead(1)
    ll.insertAtTail(3)
    ll.insertAtHead(0)
    
    #ll.insertAtPos(0,0)
    ll.display()
    ll.deleteAtTail()
    ll.display()
    ll.deleteAtHead()
    ll.display()
    #ll.deleteAtPos(1)
    ll.display()
        
            

