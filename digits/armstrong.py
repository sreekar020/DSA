# method -1 converting into string (Better for understanding and learning armstrong not good for interviews)

# n = str(int(input()))
# l = len(n)
# total = 0
# for i in n:
#     total += int(i)**l
# print(total)


# method - 2 using math operations like modulus(%) and floor division (//) best for interviews

n = int(input())
temp = n
total = 0
m = len(str(n))

while temp > 0:
    a = temp %10
    total += a**m
    temp = temp//10 
print(total)    

