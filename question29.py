# Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
n = int(input("enter a number:"))
i = 1
sum = 1
sum1 = 0
while i<=n:
    sum = sum*i
    sum1+=sum
    i+=1
print(sum1)
