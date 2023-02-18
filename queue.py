class queueArray:

    def __init__(self,size):
        self.size = size
        self.count = 0
        self.arr = []

    def enqueue(self,val):
        if (self.count>=self.size):
            print("queue overflow")
            return
        else:
            self.arr.append(val)
            self.count+=1


    def dequeue(self):
        if (self.count==0):
            print("Empty queue")
            return
        else:
            del self.arr[0]
            self.count-=1

    def display(self):
        if (self.count==0):
            print("Empty queue")
            return
        else:
            for ele in self.arr:
                print(ele,"-",end="")
            print(" None")



# Implementing Queue using Linked list

class node:
    def __init__(self,val):
        self.data = val
        self.next = None

class queueLinkedList:

    def __init__(self,size):
        self.size = size
        self.count = 0
        self.head = None
    
    def llenqueue(self,val):
        if (self.count>=self.size):
            print("Queue Overflow")
            return
        else:
            if (self.head==None):
                self.head = node(val)
                self.count+=1

            else:
                temp = self.head
                newnode = node(val)
                while(temp.next is not None):
                    temp = temp.next
                temp.next = newnode
                self.count+=1

    def lldequeue(self):
        if (self.count == 0):
            print("Empty Queue")
            return
        else:
            if (self.head.next is None):
                self.head = None
                self.count-=1
            else:
                temp = self.head
                temp = temp.next
                self.head = temp
                self.count-=1
                
    def lldisplay(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,"->",end="")
            temp = temp.next
        print("None")





if __name__ == "__main__":
    qu = queueLinkedList(3)
    qu.lldequeue()
    qu.llenqueue(1)
    qu.llenqueue(2)
    qu.lldisplay()
    qu.llenqueue(3)
    qu.llenqueue(4)
    qu.lldequeue()
    qu.lldisplay()
        