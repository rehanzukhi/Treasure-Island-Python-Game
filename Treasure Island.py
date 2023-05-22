# The code is a Python program that implements a text-based adventure game called "Treasure Island".
# The `print()` function is used to display a large ASCII art image of a treasure map at the beginning
# of the game. The game then prompts the user to make choices by entering text input using the
# `input()` function. The program uses conditional statements (`if`, `elif`, `else`) to determine the
# outcome of the game based on the user's choices. The game has multiple paths and endings, and the
# user can win or lose depending on their choices.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome To Treasure ISLAND")
print("Let's Start the Game")
op1=input("You are at a crossroad, where do you want to go?  Type 'left' or 'right'\n").lower()
if op1 == "right":
    print("Fallen into a hole, Game Over!\n")
elif op1=="left":
    print("Step 1 taken ")
    choice2= input("Do you want to swim or wait?\n").lower()
    if choice2== "swim":
        print("Attacked by Trout. Game Over\n")
    elif choice2=="wait":
        print("Next step taken. ")
        choice3=input("Choose a door. Red, Yellow or Blue?\n").lower()
        if choice3=="red":
            print("Burned By Fire Game Over!\n")

        elif choice3=="blue":
            print("Burned By Fire Game Over!\n")

        elif choice3=="Yellow":
            print("You win!\n")
    
else:
    print("Game Over!\n")
 
    
    
