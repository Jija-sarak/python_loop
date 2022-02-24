# Write a program to check whether a number is Armstrong or not. 
# (Armstrong number is a number that is equal to the sum of cubes 
# of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
# In the range 0 to 999 there exists six Armstrong numbers- 0, 1, 153, 370, 371 and 407 . 

n = int(input("enter a number:"))
j = n
sum= 0
while j>=1:
    i= j%10
    sum = sum+(i**3)
    j//=10
if sum == n:
    print("it is a armstrong number")
else:
    print(sum,"it is not a armstrong number")