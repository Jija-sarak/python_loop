# Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ 
num = int(input("enter a number:"))
i = 1
while i <= num:
    print("2"*i,end=" ")
    i+=1
print()