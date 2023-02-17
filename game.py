# this program demonstrates a guessing game
from random import randint

# get user input
player=input("what's your name?  :")
print("Hello there "+ player + "!")

# generate a random number

random_number= randint(10 , 50 )

# using a while loop
counter  = 0
while counter < 5:
    user_number = eval(input("Enter a number :"))
    counter += 1


# check if user input is equal to generated number
    if user_number < random_number:
        print("Your guess is too low , Try again")
    elif user_number > random_number:
        print("Your number is too high. ") 
    elif user_number == random_number:
        print("you win!! Nice Guess")
        break


if user_number==random_number:
    print()
else:
    print("You lose!! The correct number was ")
    print(random_number)