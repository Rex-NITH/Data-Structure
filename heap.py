class minHeap:
    def __init__(self,capacity):
        self.lst = []
        self.capacity = capacity
        self.size =0

    def isParent(self,ind):
        if ((ind-1)//2 >= 0):
            return True
        else:
            return False

    def parent(self,ind):
        return (ind-1)//2

    def leftChild(self,ind):
        return (2*ind + 1)

    def rightChild(self,ind):
        return (2*ind + 2)

    def push(self,val):
        if self.size==self.capacity:
            print("Heap is full")
            return
        elif self.size==0:
            self.lst.append(val)
            self.size+=1
            return
        else:
            self.lst.append(val)
            self.size+=1
            self.heapifyUp(self.size-1)
        
    def getMin(self):
        if self.size==0:
            print("Heap is Empty")
            return
        minn = self.lst[0]
        self.lst[0] = self.lst[self.size-1]
        self.size-=1
        self.heapifyDown(0)
        return minn

    
    def swap(self,x,y):
        temp = self.lst[x]
        self.lst[x] = self.lst[y]
        self.lst[y] = temp
    
    def display(self):
        i = 0
        while(i<self.size):
            print(self.lst[i],end=" ")
            i+=1
        print("\n",end="")

    def heapifyUp(self,ind):
        if (ind-1)//2 >= 0:
            pnod = (ind-1)//2
            if (self.lst[ind]>self.lst[pnod]):
                return
            else:
                self.swap(ind,pnod)
                self.heapifyUp(pnod)
        else:
            return
        
    def heapifyDown(self,ind):
        if (2*ind+1)<=self.size:
            cind = 2*ind+1
            if (2*ind+2 <= self.size and self.lst[cind]>self.lst[cind+1]):
                cind = cind+1
            self.swap(ind,cind)
            self.heapifyDown(cind)
        else:
            return




def main():
    obj = minHeap(5)
    obj.push(3)
    obj.push(2)
    obj.push(1)
    obj.display()
    obj.push(5)
    obj.push(6)
    obj.push(0)
    obj.display()
    val = obj.getMin()
    print(val)
    obj.display()
    

if __name__ == "__main__":
    main()
