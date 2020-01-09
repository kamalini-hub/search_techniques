arr=[5, 7, 30, 2, 156]
def search(arr, n, key):
    flag = 0
    for i in range(n):
        if(arr[i]==key):
            flag = 1
            break;
    if (flag == 1):
        print("key element found")
    else:
        print("key element not found")

search(arr, 5, 2)