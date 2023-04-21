import math
import random
import sys

def didyouwin(compAns, inp):
    if compAns == 1:
        compAns = 'r'
        if inp == 'r':
            return "Tie"
        elif inp == 's':
            return "Loss"
        else:
            return "Win"
    elif compAns == 2:
        compAns = 'p'
        if inp == 'p':
            return "Tie"
        elif inp == 'r':
            return "Loss"
        else:
            return "Win"
    else:
        compAns = 's'
        if inp == 's':
            return "Tie"
        elif inp == 'p':
            return "Loss"
        else:
            return "Win"

you = 0
comp = 0
print("Score: You - 0 | Computer - 0")
inp = input("Type r for rock, p for paper, and s for scissors: ")
print(inp)

compAns = random.randint(1,3)
opponent = didyouwin(compAns, inp)
if opponent == "Win":
    you+=1
    print("You won!")
elif opponent == "Tie":
    print("Tie!")
else:
    comp+=1
    print("You lost!")

inp = input("Go again? Type r for rock, p for paper, and s for scissors. Type q to quit:")

while inp != 'q':
    compAns = random.randint(1,3)
    opponent = didyouwin(compAns, inp)
    if opponent == "Win":
        you+=1
        print("You won!")
    elif opponent == "Tie":
        print("Tie!")
    else:
        comp+=1
        print("You lost!")
    
    inp = input("Again? Type r for rock, p for paper, and s for scissors. Type q to quit: ")

print("Final Score: You - {0} | Computer - {1}".format(str(you),str(comp)))