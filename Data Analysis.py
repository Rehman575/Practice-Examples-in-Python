#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[13]:


df = pd.read_csv('./gapminder.tsv', sep='\t' )
df.head()


# In[14]:


# Check All columns in Dataset
df.columns


# In[15]:


# Check Index Info
df.index


# In[16]:


df.values


# In[17]:


# check type

type(df)


# In[18]:


# Know the number of ROws and Columns
df.shape


# In[24]:


# Check Single COloumn
country_df = df['country']
country_df.head()


# In[23]:


type(country_df)


# In[25]:


subset = df[['country', 'continent', 'year']]


# In[27]:


subset.head(10)


# In[29]:


df.head(10)


# In[34]:


# Three different ways to slect rows

# 1 with loc (location)

df.loc[[15, 115]]


# In[36]:


# 2nd Way iloc
# We are searcing by Index number
df.iloc[[15, 10]]


# In[44]:


subset = df.loc[:,['country', 'year','gdpPercap']]


# In[45]:


subset.head(10)


# In[62]:


# Extract Data with Condition with multiple columns
df.loc[df['country'] == 'Pakistan', ['year', 'pop', 'gdpPercap'],]


# In[54]:


# Extract data with multiple conditions and multiple columns
df.loc[(df['country'] == 'Pakistan') & (df['year'] > 2005), ['year', 'pop', 'gdpPercap']]


# In[ ]:


df.

