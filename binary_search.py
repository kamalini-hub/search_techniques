def binary_search(arr, n, key):
    flag=0
    l=0
    u=n
    for i in arr:
        mid = (l+u)/2
        if(arr[mid]==key):
            flag=1
            break
        elif(arr[mid]<key):
            l=mid
        else:
            u=mid
    
    if(flag==1):
        print("key element found")
    else:
        print("key element not found")


arr=[10, 20, 30, 40, 50]
binary_search(arr, 5, 40)