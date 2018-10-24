import os    # for clearing console

arr = []


def inputArr():       # input for array
    n = int (input("Enter the maximum size of array "))
    for i in range(n):
        x = int(input())
        arr.append(x)
    os.system('cls')
    print("Entered array is ",arr)

def search():    # searching function
    print("1.by element \n2.by index")
    ch = int(input("Enter choice"))
    os.system('cls')
    if(ch==1):
        ele = int(input("Enter the element"))
        try:
            i = arr.index(ele)
            print(arr[i], i)
        except:
            print("Element not found")
       
    else:
        try:
            ind = int(input('Enter the index'))
            print(arr[ind])
        except:
            print("Index out of bound")
        

def addElement():
    print("1.Add at begining\n2.Add at end\n3.Add at specific index")
    ch = int(input("Enter your choice"))
    os.system('cls')
    ele = int(input("Enter element"))
    if(ch==1):
        arr.insert(0,ele)
    elif(ch==2):
        arr.append(ele)
    else:
        ind = int(input("Enter index"))
        arr.insert(ind,ele)
    print(arr)

def remove():
    try:
        ind = int(input("Enter index"))
        arr.pop(ind)
    except:
        print("Index out of bound")
    print(arr)

def sort():
    arr.sort()
    print(arr)


inputArr()
while(True):
    print("----------Operations---------")
    print("1.Search\n2.Add Element\n3.Sort\n4.Remove element\n5.New Array\n6.Exit\n")
    ch = int(input("Enter your choice"))
    os.system('cls')
    if(ch==1):
        search()
       
    elif(ch==2):
        addElement()
        
    elif(ch==3):
        sort()
    elif(ch==4):
        remove()
        
    elif (ch==6):
        exit()
        








