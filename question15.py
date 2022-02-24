# Write a program to print the Fibonacci series till n terms (Accept n from user)
# Fibonacci series is shown here, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
n = int(input("enter a number:"))
i = 0
j = 1
while i<=n:
    print(i)
    print(j)
    i = i+j
    j = j+i
