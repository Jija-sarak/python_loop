# Write a program to reverse the number accepted by the user.
num = int(input("enter a number:"))
i = 0
while num>0:
    print(num%10,end="")
    num = num//10
print()