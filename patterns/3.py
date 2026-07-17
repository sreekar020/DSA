# pattern 3

# * * * * *
# * * * *
# * * * 
# * *
# *

def pattern3(n):
    for i in range(n+1):
        for j in range(n-i):
            print("*",end=" ")
        print()

pattern3(int(input()))            