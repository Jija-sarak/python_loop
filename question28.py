# Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
n = int(input("enter a number:"))
i = 1
sum = 0
while i<=n:
    a = i**3
    sum=sum+a
    i+=1
print(sum)
