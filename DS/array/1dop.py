import os
arr = []
n= int (input("Enter the maximum size of array "))
for i in range(n):
    x = int(input())
    arr.append(x)

print("Entered array is ",arr)
def search():
    print("1.by element \n2.by index")
    ch = int(input("Enter choice"))
    os.system('cls')
    if(ch==1):
        ele = int(input("Enter the element"))
        for i in range(n):
            if arr[i]==ele:
                print(arr[i],i+1)
    else:
        ind = int(input('Enter the index'))
        print(arr[ind])
search()


