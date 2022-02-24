# Write a program to find the product of the digits of a number accepted from the user.
num = int(input("enter a number:"))
product = 1
temp = num
while temp!=0:
    product = product*(temp%10)
    print(temp%10)
    temp = int(temp/10)
print("num:",num,"product",product)
