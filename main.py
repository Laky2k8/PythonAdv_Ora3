import math
import random

print("PYTHON ADVANCED CLASS 3")
print("----------------------- \n \n")

print("TASK 1 \n")
r = int(input("Please give me a number! I will compute the area and circumference of a circle with this diameter. \n"))

cArea = r*r*math.pi
cCircum = 2*r*math.pi

print("The area is", str(cArea), ", the circumference is", str(cCircum),"units.")



print("\n \n TASK 2 \n")

evenList = []

for i in range(100):
    evenList.append(random.randrange(0,9,2))

print("A list of 100 random even numbers from 0 to 8: ", evenList)

print("\n \n TASK 3 \n")

num1 = random.randint(0,100)
guessedRight = False
print("I thought of a number. Guess it!")

while guessedRight == False:
    guessNum = int(input("Guess: "))
    if guessNum > num1:
        print("My guessed number is smaller! Try again!")

    elif guessNum < num1:
        print("My guessed number is larger! Try again!")

    elif guessNum == num1:
        print("You did it! The guessed number was", num1, "!")
        guessedRight = True



