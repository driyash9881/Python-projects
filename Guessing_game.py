import numbers
import random

#  = random.randint(5,11)
# print(durgesh)
top_of_range = input("Entre a number:  ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please enter number greater than 0 next time. ")
        quit()
else:
    print("Please enter digit next time. ")
    quit()
    
random_number = random.randint(0 , top_of_range)
guesses = 0

                                                                                                                                                              
while True:
    guesses += 1
    user_guess = input("guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:  
        print("Please enter digit next time. ")
        continue

    if user_guess == random_number:
        print("You got it :) ")
        break 
    
    elif user_guess > random_number:
            print("you were above the number")
    else:
            print("you were below the number")
         
print("You got it in" , guesses , "guesses")

review = input("you like the game? yes or no ").lower()
if review == "yes":
    rate = int(input("please rate this under 5: "))
    if rate >= 5:
        print("excellent")
    elif rate>=4:
        print("very good")
    elif rate>=3:
        print("good")
    elif rate>=2:
        print("poor")
    elif rate>=1:
        print("worst")
    else:
        print("i don't like it at all please make changes!!")
else:
    type_opnion = input("type what your opnion ")
    print(type_opnion)

    