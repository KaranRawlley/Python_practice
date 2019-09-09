""" 
    queue is FIFO data structure
    in which insertion takes place at rear end
    and removal takes place at front end
"""

class queue:
    def __init__(self,data):
        self.data=data
        self.next=None
rear = front = queue(10)

def enqueue(data):
    global rear
    global front
    temp = queue(data)
    if front==None and rear ==None:
        rear=temp
        front=temp
        temp.next=None
    elif front==rear:
        front.next=temp
        rear=temp

    else:
        rear.next=temp
        rear=temp

def dequeue():
    global front
    global rear
    if front==rear:
        x = front.data
        temp=front
        front=None
        rear=None
        del temp
        return x
    else:
        x = front.data
        temp=front
        front=front.next
        del temp
        return x

# if __name__=="__main__":

#     enqueue(23)
#     enqueue(98)
#     enqueue(78)
#     enqueue(67)
#     enqueue(25)
#     temp = rear
#     # while temp.next!=None:
#     #     print(temp.data)
#     #     temp=temp.next


#     # y=dequeue()
    
#     # x=dequeue()
#     temp=front
#     while temp:
#         print(temp.data)
#         temp=temp.next
    

