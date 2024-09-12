#!/usr/bin/env python
# coding: utf-8

# In[11]:


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
x = int(input(f"what do you choose? 0 for Rock,1 for Paper, 2 for Scissors- "))
y = random.randint(0,2)
if x == 0:
    print("You choose rock- ",rock)
elif x == 1:
    print("You choose paper- ",paper)
elif x == 2:
    print("You choose scissors- ",scissors)
else:
    print("Wrong input")


print(y)
if y == 0:
    print("Computer choose rock- ",rock)
elif y == 1:
    print("Computer choose paper- ",paper)
else:
    print("Computer choose scissors- ",scissors)

if x == y:
    print("Draw")
elif x == 0 and y == 1:
    print("Computer Win")
elif x == 0 and y == 2:
    print("You win")
elif x == 1 and y == 0:
    print("You win")
elif x == 1 and y == 2:
    print("Computer win")
elif x == 2 and y == 0:
    print("Computer win")
else:
    print("You win")


# In[ ]:




