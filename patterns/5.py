# pattern 5

# *
# * *
# * * *
# * * * * 
# * * * * * 
# * * * *
# * * * 
# * *
# *


# optimal code

def pattern5(n):
    for i in range(1,n*2):
        x = n-(i-n) if i>=n else i
    for j in range(1, x+1):
            print("*", end=" ")
    print()
         
    
pattern5(int(input()))            





# for c in range(1,n+1):    
    #     for k in range(n-c):
    #         print("*", end=" ")
    #     print()    