""" linked list implementation of stack 
    Stack is a LIFO data structure
    insertion and deletion both from the top of the stack.
    in O(1) time.
"""

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

top = node(30)

def pop():
    global top
    if top==None:
        return top
    temp = top
    top = top.next
    x = temp.data
    del temp
    return x


def push(data):
    global top
    #print(top)
    temp = node(data)
    temp.next=top
    top=temp
    
    #print(top)

def isempty():
    global top
    if top==None:
        return True
    else :
        return False

def topi():
    global top
    return top.data

if __name__=="__main__":

    
    push(34)
    push(45)
    push(32)
    push(56)
    push('gfg')
    push(89)

    print(topi())

    print(pop())

    root=top
    while root!=None:
        print(root.data)
        root=root.next

    

