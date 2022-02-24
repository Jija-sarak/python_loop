for i in range (5):
    for j in range (7):
        if i==0 and j%3!=0 or i==1 and j%3==0  or i-j==1 or i+j==7:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()              
    
    # a = "don't expect to get what you give"
# i = 0
# list1=[]
# while i < len(a):
#     j =0
#     c =0
#     while j< len(a):
#         if a[i] == a[j]:
#             c+=1
#         j+=1
#     if a[i].isalpha():
#         if a[i] not in list1:
#             list1.append(a[i])
#             print(a[i],"=",c)
#     i+=1
a = "don't expect to get what you give"
i = 0
c = 0
d = 0
while i < len(a):
    if a[i] == "a" or  a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        c+=1
    else :
        if a[i].isalpha():
            d+=1
    i+=1
print( " wovels","=",c,"\n","consonants","=",d)

