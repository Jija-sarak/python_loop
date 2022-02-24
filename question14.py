#  Write a program to display the number names of the digits of if the number is 231 
# then output should be Two a number entered by user, for example Three One
num = int(input("enter a number:"))
n = str(num)
i = 0
while i<len(n):
    a = int(n[i])
    if a == 0 :
        print("Zero",end=" ")
    if a == 1:
        print("One",end=" ")
    if a == 2:
        print("Two",end=" ")
    if a == 3:
        print("Three",end=" ")
    if a == 4:
        print("Four",end=" ")
    if a == 5:
        print("Five",end=" ")
    if a == 6:
        print("Six",end=" ")
    if a == 7:
        print("Seven",end=" ")
    if a == 8:
        print("Eight",end=" ")
    if a == 9:
        print("Nine",end=" ")
    i+=1
print()
    