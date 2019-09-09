import './queue.py'
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insert(root,data):
    if root==None:
        root = node(data)
        
    elif data<=root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root


def search(root,data):
    if root==None:
        return False
    elif root.data==data:
        return True
    elif root.data>=data:
        return search(root.left,data)
    else:
        return search(root.right,data)
 


def findMax(root):
    current = root
    while current.right != None:
        current=current.right
    return current.data


def findMin(root):
    current = root
    while current.left!=None:
        current=current.left
    return current.data



def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)



def preorder(root):
    if root==None:
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)



def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')



def height(root):
    if root==None:
        return -1
    lefth = height(root.left)
    righth = height(root.right)
    return max(righth,lefth)+1


def Minf(root):
    current = root
    while current.left!=None:
        current=current.left
    return current



def delete(root,data):
    if root==None:
        return root
    elif data<root.data:
        root.left = delete(root.left,data)
    elif data>root.data:
        root.right = delete(root.right,data)
    else:
        # Case 1 - no child
        if root.left==None and root.right==None:   
            del root
            root=None
        # Case 2 - left or right child
        elif root.left==None:
            temp = root
            root = root.right
            del temp
        elif root.right==None:
            temp = root
            root = root.left
            del temp
        # Case 3 - both left and right child
        else:
            temp = Minf(root.right)
            root.data = temp.data
            root.right=delete(root.right,temp.data)
    return root

def bfs(root):
    if root==None:
        return
    front=rear=queuep(root)



if __name__=="__main__":
        
    
    # initializing root node

    root = node(20)

    # inserting values into bst

    insert(root,4)
    insert(root,7)
    insert(root,10)
    insert(root,56)
    insert(root,1)
    insert(root,32)
    insert(root,67)
    insert(root,6)
    insert(root,9)
    insert(root,8)



    # inorder(root)       # inorder traversal
    # print("\n")
    # postorder(root)     # postorder traversal
    # print('\n')
    # preorder(root)      # preorder traversal
    # print('\n')
    # print(height(root)) # height of tree

    # root = delete(root,1)   # deleting a node

    # inorder(root)
    # print("\n")
    # postorder(root)
    # print('\n')
    # preorder(root)
    # print('\n')
    # print(height(root))

