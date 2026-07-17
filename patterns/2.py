# pattern 2
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *


def pattern2(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

pattern2(int(input()))        