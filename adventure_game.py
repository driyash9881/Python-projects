name = input("Enter your name:  ")

print("Are you ready for the adventure?  ",name)

start = input("We started the game and it is not easy!! Which path you wanna choose to start the game left or right choose wisely  ").lower()
  
if start == "left":
    start = input("you want chettah to run fast or lion to eat all our enemies!! choose your optiom eat or run  ").lower()
    if start ==  "eat":
        print("The lion was bitten by elephant and you lose! ")
    elif start == "run":
        print("by running so far the cheetah got hit by the buleet you loose ")
    else:
        print("you have selected invalid option !! please select valid option next time. ")
        quit()
elif start == "right":
    start = input("You came to bridge , it looks wobbly , do you want to cross it or head back(cross/back)").lower()
    if start == "back":
        print("if the answer is back to the start point and you lose!!  ")
    elif start == "cross":
        start = input("you cross the bridge and meet the stranger do you want to talk to them (Yes /no)  ").lower()
        if start == "yes":
            print("you talked to the stranger and they gave you gold!! YOU WIN!!!")
        elif start == "no": 
            print("you ignored the  stranger and you lose!!")
        else:
            print("you haven;t choose valid answer!!")
    else:
        print("you have choose wrong answer. now you have to quit this game please choose correct next time.")
else:
    print("you have opt for wrong answer i am sorry you have to quit this game!! matane minasas ")
    quit()
