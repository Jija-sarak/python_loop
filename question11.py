# Write a program to find the sum of the digits of a number accepted from the user.
num = int(input("enter a number:"))
sum = 0
while num>0:
    a = num%10
    sum=sum+a
    num//=10
print(sum)
