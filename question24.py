# Write a program to display sum of odd numbers and even numbers separately that fall between two numbers 
# accepted from the user.(including both numbers) 100 and 500.
num = int(input("enter a number:"))
num1 = int(input("enter a number:"))
sum_even = 0
sum_odd = 0
while num<=num1:
    if num%2==0:
        sum_even=sum_even+num
    else:
        sum_odd = sum_odd+num
    num+=1
print("sum of even numbers :",sum_even)
print("sum of odd numbers :",sum_odd)