# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
J = int(input("enter a number:"))
A = int(input("enter a number:"))
sum = A+J
if sum>=15 and sum<=20:
     print(20)
else:
    print(sum)