#!/usr/bin/env python
# coding: utf-8

# In[3]:


def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
is_prime(13)


# In[ ]:




