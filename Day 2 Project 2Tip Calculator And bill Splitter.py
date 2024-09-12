#!/usr/bin/env python
# coding: utf-8

# In[34]:


print("Welcome to the tip calculator and bill splitter")
bill = int(input("Enter the boll Amount ? $"))
tip = int(input("Enter the tip in percentage which you want to give? "))
final_bill = bill*tip/100+bill
print("Your final bill amount is $ ",final_bill)
people = int(input("enter the number of people in which you want to split the bill? "))
share_per_person = final_bill/people
final_amount = round(share_per_person, 2)
print("share for per person is $",final_amount)


# In[ ]:




