#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


garden = np.random.randint(1,10,(3,3))


# In[3]:


garden


# In[4]:


def eat_zanoria(garden):
    # start at the origin, garden[2][2]
    # chomp away; up, down, left, right, searching for the most carrots in your path
    # the path in the mocked up matrix would be: 
    # garden[1][1] -> garden[1][2] -> garden[0][2] -> garden[0][1] -> garden[0][0] -> garden[1][0] ->
    # garden[2][0] -> garden[2][1] -> garden[2][2] -> sleep
    
    # this resembles DAG problems, I've seen before but haven't encountered, likely involves
    # 1) detecting the origin at garden[1][1]
    # 2) taking the abs_diff(garden[1][1] - garden[ni][mi]), for each row, column value and selecting
    # the "path" where the abs_diff is the greatest in the search space of up, down, left, right
    return


# In[ ]:




