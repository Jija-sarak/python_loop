# Write a program to check whether a number is palindrome or not.
n = int(input("enter a number:"))
num = n
sum = 0
while num > 0:
    a= num%10
    sum =str(sum) + str(a)
    num//=10
if n == int(sum):
    print("it is a palindrome number")
else:
    print("it is not a palindrome")

