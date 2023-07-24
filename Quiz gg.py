#quiz_game

print("Hey welcome to my quiz!! ")
ask = input("do you want to play? ")
if ask.lower() != "yes":
    quit()

print("lets play hifi :) ")
score = 0

answer = input("what is cpu full form? \n")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
    score = score + 1
else:
    print("incorrect")

answer = input("what is html and css? \n ")
if answer.lower() == "scripting language":
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")
answer =input("how to save the extention file of c++ ? \n") 
if answer.lower() == "cpp":
    print("correct")
    score +=1
    score = score + 1
else: 
    print("incorrect")
answer =input("how to save the extention file of python? \n") 
if answer.lower() == "py":
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")
answer = input("what are types of loops in python? \n")
if answer.lower() == "while and for" :
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")
answer  = input("IS there is diffrence between java and javascript? \n")
if answer.lower() == "yes":
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")
answer = input("IS there is diffrence between web development and andriod development? \n")
if answer.lower() == "yes":
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")
answer = input("what is use of if and else? \n ")
if answer.lower() == "true or false":
    print("correct")
    score +=1
    score = score + 1
else:
    print("incorrect")

print("Your score is " + str(score) + " you have got this much right answer")
print("Your percentage is " + str((score/14)*  100) + " percentage")
