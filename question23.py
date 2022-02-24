# Write a program to accept 10 numbers from the user and display the largest & smallest number.
i = 0
n = int(input("enter a number :"))
min = n
max = n
while i < 9:
    n  =int(input("enter a number"))
    if max<n:
        max=n
    if min > n:
        min = n
    i+=1
print(max)
print(min)


