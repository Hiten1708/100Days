print('''
Welcome to the game of treasure island, do what you can to survive...

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
              ''')


print("Welcome to Treasure Island. Your mission is to find treasure.")

choice1 = input("You have now finally arrived on Treasure Island but you see two path, one to the right and one to the left. Which one would you choose? Type 'Right' or 'Left'. \n").lower()

if choice1 == "left":
  choice2 = input("You have arrived on a riverside. You can either choose to wait for friend to cross and come back or you can choose to swim across without waiting. Type 'Swim' or 'Wait'\n").lower()
  if choice2 == "wait":
    choice3 = input("You have arrived at a house which has three colored doors: 'Red','Yellow','Blue'. Which one would you choose?\n").lower()
    if choice3 == "yellow":
      print("You Won. You arrived on your destination.")
    else:
      print("You died. Game Over.")
  else:
    print("You were killed by a shark")
else:
  print("You fell into a pit. You died. Game Over")