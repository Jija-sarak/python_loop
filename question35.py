# Write a program to print the factorial of a number.
num = int(input("enter a number :"))
factorial = 1
while num>0:
    factorial*=num
    num-=1
print(factorial)
    