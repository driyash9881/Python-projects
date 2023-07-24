import random

user_wins = 0
computer_wins = 0

option = ["rock" ,  "paper" , "scissors"]


while True:
    user_input = input("Type rock/paper/scissors or q to QUIT:  ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue
    random_numbers = random.randint(0 , 2)
    # rock:0 , paper:1 , scissors:2 
    computer_picked= option[random_numbers]  
    print("Computer picked" , computer_picked + ".")

    if user_input == "rock" and computer_picked == "scissors":
        print("you win!!")
        user_wins += 1
    elif user_input == "paper" and computer_picked == "rock":
        print("you win!!")
        user_wins += 1
    elif user_input == "scissors" and computer_picked == "paper":
        print("you win!!")
        user_wins += 1
    elif user_input == computer_picked:
        print("Its a tie.")
        continue
    else:
        print("COMUTER WON!!")
        computer_wins +=1
    
print("YOU WIN" , user_wins )
print("COMPUTER WIN" , computer_wins )

print("Mata'ne")
print("REVIEW TIME!! HEYY HELP ME TO IMPROVE :)")
review = input("You liked this game ! yes or no: ").lower()
if review == "yes":
    print("arigato'ne")
else:
    print("we are sorry i will try to improve and make it more better for you")

    
