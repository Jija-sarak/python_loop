# Write a Python program to guess a number between 1 to 9
import random
ran=random.randrange(1,10)
guess=int(input("guess the number"))
print(ran)
for i in range(ran):
    if guess==ran:
        print("you won")
        break
    elif guess>ran:
        print("high")
        break
    elif guess<ran:
        print("low")
        break

