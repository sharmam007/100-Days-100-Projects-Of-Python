#!/usr/bin/env python
# coding: utf-8

# In[13]:


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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
direction = str(input("Choose your direction Left or Right- "))
if direction == "Left" or direction =="left":
    task1 = input("would you like to swim or wait- ")
    if task1 == "Swim" or task1 == "swim":
        print("Attacked by trout. Game Over")
    elif task1 == "wait" or task1 == "Wait":
        task2 = input("Which door would you like to choose Red,Blue or Yellow ?- ")
        if task2 == "blue" or task2 == "Blue":
            print("Eaten by beasts. Game Over")
        elif task2 == "red" or task2 =="Red":
            print("Burned by Fire. Game over")
        elif task2 == "yellow" or task2 == "Yellow":
            print("Yehhhh Congratulations you WIN.")
else:
     print("Fall into a hole. Game Over")


# In[ ]:




