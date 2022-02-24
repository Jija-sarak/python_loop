#  Write a program to check whether a number is prime or not.
# num = int(input("enter a number:"))
# i = 2
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==1:
#     print("it is a prime number")
# else:
#     print("it is not a prime number")
    
i = 2
count1 = 0
while i < 100:
    j = 2
    c = 0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==1:
        print(i)
    i+=1
