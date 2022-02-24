# Write a program to display all even numbers that fall between two numbers (exclusive both numbers) entered by the user.
num = int(input("enter a number:"))
num1 = int(input("enter a number:"))
while num <num1:
    num+=1
    if num%2==0 and num!=num1:
        print(num)
    