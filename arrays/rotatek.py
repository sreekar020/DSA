# # rotate left the no.of elemnts 
# def a(arr, n, k):
#     for i in range(k):
#         temp = arr[0]
#         for j in range(len(arr)-1):
#             arr[j] = arr[j+1]
#         arr[-1] = temp
#     return arr
# n = int(input())
# k = int(input())%n
# arr = list(map(int,input().split(" ")))
# print(a(arr,a,k))



# optimal code
# def a(arr, n, k):

# for i in range(k):
        #     temp = arr[0]
        #     for j in range(len(arr)-1):
        #         arr[j] = arr[j+1]
        #     arr[-1] = temp
        # return arr 


def reverse(left,right,arr):
    while left<right :
        arr[left],arr[right] = arr[right],arr[left]
        left+=1 
        right-=1
def leftRotate(arr, n, k):
    reverse(0, k-1, arr)
    reverse(k, n-1, arr)
    reverse(0, n-1 , arr)
    return arr
n = int(input())
k = int(input())%n
arr = list(map(int,input().split(" ")))
print(leftRotate(arr,n,k))
