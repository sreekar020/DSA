def a(arr, n):
    temp = arr[0]
    for i in range(0, 4):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return arr    
n = int(input())
arr = list(map(int,input().split(" ")))
print(a(arr,a))
