n = int(input())
temp = n 
b = 0
while temp > 0 :
   a = temp%10
   b = a + (10*b)
   temp = temp//10

if a == b:
    print("Palindrome")
else:
    print("Not palindrome")       