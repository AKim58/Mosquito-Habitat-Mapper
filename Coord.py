#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install glob
#!pip install pandas
#!pip install requests


# In[4]:


import glob
import pandas as pd
import numpy as np
import os


# In[7]:


pd.__version__


# In[5]:


#data found from this website: https://datasearch.globe.gov/

data = pd.read_csv('SEESMosquito_Data.csv')

#filtering out specific columns from data

col = ['mosquito habitat mapper:userid',
       'mosquito habitat mapper:larvae count',
       'mosquito habitat mapper:measurement latitude',
       'mosquito habitat mapper:measurement longitude']

coord = ['mosquito habitat mapper:userid',
       'mosquito habitat mapper:measurement latitude',
       'mosquito habitat mapper:measurement longitude']

df = pd.DataFrame(data, columns=col)

#removing all datasets where a value was missing (appear as nan on raw dataset)
#id_count.dropna(inplace=True)
df = df.dropna()
df = df.reset_index(drop=True)

#removing all 0s in mosquito count
df.drop(df.loc[df['mosquito habitat mapper:larvae count']==0].index, inplace=True)

#convert the larvae count and id to int
df['mosquito habitat mapper:larvae count'] = pd.to_numeric(df['mosquito habitat mapper:larvae count'], downcast='integer')
df['mosquito habitat mapper:userid'] = pd.to_numeric(df['mosquito habitat mapper:userid'], downcast='integer')



# In[6]:


df


# In[31]:


df.to_csv(r'MM_Points_nonzero.csv', index = False)


# In[ ]:




