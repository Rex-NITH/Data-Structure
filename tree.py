class node:
    def __init__(self,val):
        self.left = None
        self.data = val
        self.right = None

class Tree:
    def __init__(self):
        pass

    def insert(self,root,val):
        if (root == None):
            newnode = node(val)
            root = newnode
            return root
        else:
            if (root.data>val):
                root.left = self.insert(root.left,val)
            elif(root.data<val):
                root.right = self.insert(root.right,val)
        return root

    def delete_leaf(self,root,val):
        if (root == None):
            return None
        elif (root.data>val):
            root.left = self.delete_leaf(root.left,val)
        elif (root.data<val):
            root.right = self.delete_leaf(root.right,val)
        else:
            if (root.left is None) and (root.right is None):
                del root
                return None
            elif(root.left == None):
                temp = root.right
                del root
                return temp
            elif(root.right is None):
                temp = root.left
                del root
                return temp
        return root

    def get_node(self,root,lst):
        if (root is not None):
            lst.append(root.data)
            self.get_node(root.left,lst)
            self.get_node(root.right,lst)
            return lst

    def delete_node(self,root,val):
        if (root == None):
            return None
        elif (root.data>val):
            root.left = self.delete_node(root.left,val)
        elif (root.data<val):
            root.right = self.delete_node(root.right,val)
        else:
            if ((root.left is not None) and (root.right is not None)):
                ltemp = root.left
                rtemp = root.right
                lst = []
                val = self.get_node(ltemp,lst)
                del root
                for ele in val:
                    self.insert(rtemp,ele)
            return rtemp
        return root



    def search(self,root,val):

        if (root == None):
            print("tree end and element not present")
            return
        elif (root.data == val):
            print("\n",root.data)
            print("element found")
            return root
        elif (root.data>val):
            root.left = self.search(root.left,val)
        elif (root.data<val):
            root.right = self.search(root.right,val)
        else:
            print("value not present in the tree")
            return




    
    def preOrder(self,root):
        if (root is not None):
            print(root.data,end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def inOrder(self,root):
        if (root is not None):
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)
    
    def postOrder(self,root):
        if (root is not None):
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=" ")



        
def main():
    root = None
    tr = Tree()
    root = tr.insert(root,6)
    tr.insert(root,8)
    tr.insert(root,9)
    tr.insert(root,4)
    tr.insert(root,3)
    tr.insert(root,5)
    tr.insert(root,7)
    tr.preOrder(root)
    # print("\n")
    # tr.inOrder(root)
    # print("\n")
    # tr.postOrder(root)
    # print("\n")
    # tr.delete_leaf(root,5)
    # tr.inOrder(root)
    # tr.search(root,10)
    tr.delete_node(root,4)
    print("\n")
    tr.preOrder(root)
    



if __name__ == "__main__":
    main()