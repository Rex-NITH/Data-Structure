import numpy as np

class stackArray:

    def __init__(self,size):
        self.size = size
        self.arr = []
    
    def push(self,val):
        
        if ((len(self.arr))<self.size):
            self.arr.append(val)
        else:
            print("Stack overflow")
            return

    def pop(self):
        if (len(self.arr)==0):
            print("Stack is empty")
            return
        else:
            del self.arr[len(self.arr)-1]
        
    def peek(self):
        if (len(self.arr)==0):
            print("Stack is empty")
            return
        else:
            print(self.arr[len(self.arr)-1])

# Implementing Stack Using Linked List

class node:
    def __init__(self,val):
        self.data  = val
        self.next = None

class stackLinkedList:

    def __init__(self,size):
        self.size = size
        self.head = None
        self.count = 0
    
    def llpush(self,val):

        if (self.count>=self.size):
            print("stack overflow")
            return 

        else:
            if (self.head == None):
                self.head = node(val)
                self.count+=1
            else:
                newnode = node(val)
                newnode.next = self.head
                self.head = newnode
                self.count+=1
       

    def llpop(self):
        if (self.count == 0):
            print("Stack is emty")
            return

        else:
            if(self.head.next is None):
                self.head = None
                self.count-=1
            else:
                temp = self.head
                temp = temp.next
                self.head = temp
                self.count-=1
        

    def llpeek(self):
        if (self.count == 0):
            print("Stack is emty")
            return

        else:
            temp = self.head
            print(temp.data)

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"->",end="")
            temp=temp.next
        print("None")
        


if __name__ == "__main__":
    st = stackLinkedList(3)
    st.llpop()
    st.llpush(1)
    st.llpush(2)
    st.llpeek()
    st.llpush(3)
    st.llpush(4)
    st.llpop()
    st.llpeek()
    st.display()

