# this program demonstrates a guessing game
from random import randint

# get user input
player=input("what's your name?  :")
print("Hello there "+ player + "!")

# generate a random number

number= randint(10 , 50)

# using a while loop
counter  = 0
while counter < 5:
    user_number = eval(input("Enter a number :"))
# generate random number

# check if user input is equal to generated number
