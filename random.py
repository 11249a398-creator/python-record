
import random
num = random.random()
num = num * 100
print(num)


import random
num = random.randint(0, 9)
print(num)


import random
num1 = random.randint(0, 1000)
num2 = random.randint(1, 1000)   # avoid division by zero!
newrand = num1 / num2
print(newrand)

# --------------------------


import random
num = random.randrange(0, 100, 5)
print(num)

# --------------------------


import random
colour = random.choice(["red", "black", "green"])
print(colour)
