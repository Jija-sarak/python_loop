#  Write a program to accept 10 numbers from the user and display it’s average.
i = 0
sum = 0
while i<10:
    num = int(input("enter a number:"))
    sum=sum+num
    average = sum/10
    i+=1
print(average)