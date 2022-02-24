# .Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included).`
A = 1500
J = 2700
while A <= J:
    if A%7==0 and A%5==0:
        print(A)
    A+=1