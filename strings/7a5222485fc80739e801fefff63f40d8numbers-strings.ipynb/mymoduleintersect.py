#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Build a function to return the intersection of two sets
# Code here:

def intersect(small_primes, fibonacci):
    my_set = set(())
    for prime in small_primes:
        if fibonacci.count(prime) != 0:
            my_set.add(prime)
    print(my_set)


# In[ ]:




