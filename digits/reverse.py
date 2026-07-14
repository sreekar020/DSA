# reverse a number


n = int(input())
temp =n
b = 0
while temp > 0:
    a = temp %10
    b = a+b*10
    temp = temp//10
print(b)
