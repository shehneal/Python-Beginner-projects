#Treasure Island game program

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
decision1 = input("You're at a crossroad. where would you go? left or right?")
decision1 = decision1.lower()
if decision1 == "left":
  decision2 = input('''There is a lake and an island in the middle of it.
                       Would you swim to the island?
                       or wait for a boat?''')
  decision2 = decision2.lower()
  if decision2 == "wait":
    decision3 = input('''There is house on Island with three doors:
                         red, yellow, blue. 
                         which door would you open?''')
    decision3 = decision3.lower()
    if decision3 == "yellow":
      print("You found the treasure. You Win!")
    elif decision3 == "red":
      print("Burned by fire. Game Over.")
    elif decision3 == "blue":
      print("Eaten by beastes. Game Over.")
    else:
        print("Game Over")
  else:
    print("Attacked by trout. Game Over.")
else:
  print ("Oopps! you fell into a hole. Game Over!")







