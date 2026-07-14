

# n = int(input())
# temp = []                            #brute force
# count = 0
# for i in range(1,n+1):
#     if n % i==0:
#         temp.append(i)
#         count+=1        
# print(count,temp)




# n = int(input())                      # better solution 
# temp = []
# count = 1
# for i in range(1,n+1//2):
#     if n % i==0:
#         temp.append(i)
#         count+=1
# temp.append(n)        
# print(count,temp)


from math import *
n = int(input())                       # optimal solution (better for interviews)
temp = []
count = 0
for i in range(1,int(sqrt(n))+1):
    if n % i==0:
        temp.append(i)
        count+=1
        if n/i != i:
            temp.append(n/i)
            count+=1
print(count,temp)        