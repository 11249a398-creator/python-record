import random
num = random.random()
num = num * 100
print(num)

import random
num = random.randint(0,9)
print(num)

import random
num1 = random.randint(0,1000)
num2 = random.randint(0,1000)
c = num1/num2
print(c)

num = random.randrange(0,200,5)
print(num)

colour=random.choice(["red","yellow","green"])
print(colour)

value=random.choice(["h","t"])
choice=input("Make your choice!!(h or t)").lower()
if value==choice:
    print("you win")
else:
    print("bad luck")
if value=="h":
    print("the computer slected heads")
elif value=="t":
    print("the computer s
colour = random.choice(["black","white", "blue", "red", "yellow"])
correct = False
while correct == False:
    guess = input("Pick one colour: black, white, blue, red, yellow ").lower()  # BLACK
    if guess == colour:
        print("Well done YOU WON GAME " )
        correct = True
    else:
        if colour == "black":
            print("You are such a BLACK luck guy.")
        if colour == "white":
            print("Too naive to choose WHITE")
        if colour == "blue":
            print("You probably feeling BLUE right now.")
        if colour == "red":
            print("Is your face looks RED right now?")
        if colour == "yellow":
            print("I bet your future is as bright as yellow.")
