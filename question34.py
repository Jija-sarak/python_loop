# Accept two numbers from the user and display sum of even numbers between them(including both)
J = int(input("enter a number:"))
A = int(input("enter a number:"))
sum = 0
while J <= A:
    if J%2==0:
        sum=sum+J
    J+=1
print(sum)