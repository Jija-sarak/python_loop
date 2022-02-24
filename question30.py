# Write a program to find the sum of following series:
# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
num = int(input("enter a number:"))
sum = 0
i = 0
while i<=num:
    if i%2==0:
        sum+=(i*i)
    else:
        sum-=(i*i)
    i+=1
print(sum)