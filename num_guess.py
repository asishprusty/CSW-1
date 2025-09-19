import random
number = random.randint(1,10)
guess= int(input("Enter a number between 1-10: "))
while guess!=number:
    guess=int(input("Wrong,Try again! "))
print("You Got it Correct")