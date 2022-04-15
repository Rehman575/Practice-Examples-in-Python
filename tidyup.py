#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('pew.csv')


# In[3]:


df.head()


# In[4]:


pew_long = pd.melt(df, id_vars = 'religion')


# In[5]:


pew_long.columns


# In[6]:


pew_long.head()

# variable and Value are default names for coloumns


# In[7]:


pew_long = pd.melt(df, id_vars = 'religion', var_name='income', value_name='count')


# In[8]:


pew_long.head()


# # Importing Billboard Dataset

# In[9]:


billboard = pd.read_csv('./billboard.csv')


# In[10]:


billboard.head()


# In[11]:


# melting Dataframe in one column, Unchanged Multiple columns
billboard_melt = pd.melt(billboard, id_vars = ['year','artist','track','time','date.entered'], var_name='week', value_name='rating')


# In[12]:


billboard_melt.head()


# In[13]:


billboard.shape


# In[14]:


billboard_melt.shape


# In[15]:



billboard_melt['rating'] = billboard_melt['rating'].fillna(0)


# In[16]:


billboard_melt.isnull().sum()


# # Importing another dataset

# In[17]:


ebula = pd.read_csv('./country_timeseries.csv')


# In[18]:


ebula.head()


# In[19]:


ebula_long = pd.melt(ebula, id_vars=['Date','Day'])


# In[20]:


ebula_long.head()


# In[21]:


'Cases_Guinea'.split('_')


# In[22]:


variable_spilt = ebula_long['variable'].str.split('_')


# In[23]:


variable_spilt


# In[24]:


type(variable_spilt[0])


# In[25]:


(variable_spilt[0][0])


# In[26]:


variable_spilt.str.get(0)


# In[27]:


variable_spilt.str.get(1)


# In[28]:


ebula_long['stats'] = variable_spilt.str.get(0)
ebula_long['country'] = variable_spilt.str.get(1)


# In[29]:


ebula_long.head()


# In[30]:


ebula_long[['stats_e','country_e']] = (ebula_long['variable']
                                       .str
                                       .split('_', expand=True))


# In[31]:


ebula_long.head()


# In[34]:


# new data set

weather = pd.read_csv('./weather.csv')
weather.head()


# In[47]:


# can use pd.melt or weather.melt
weather_melt = pd.melt(
            weather, id_vars=['id','year','month','element'],
            var_name='day',
            value_name='temp')


# In[48]:


weather_melt.head()


# In[51]:


weather_tidy = weather_melt.pivot_table(
        index=['id','year','month','day'],
        columns='element',
        values='temp'
)


# In[53]:


weather_tidy.reset_index()


# In[56]:


# Billborad Dataset

billboard_melt.head()


# In[57]:


billboard_melt.loc[billboard_melt['track'] == 'Loser']


# In[62]:


billboard_song = billboard_melt[['year','artist','track','time']]


# In[64]:


billboard_song.head()


# In[66]:


billboard_song.shape


# In[70]:


billboard_song = billboard_song.drop_duplicates()


# In[72]:


billboard_song.head()


# In[73]:


billboard_song.shape


# In[74]:


billboard_song['id'] = range(len(billboard_song))


# In[75]:


billboard_song.head()


# In[77]:


billboard_song.to_csv('billboard_song.csv', index=False)


# In[78]:


billboard_ratings = billboard_melt.merge(
    billboard_song, on=['year','artist','track','time']

)


# In[80]:


billboard_ratings.head()


# In[82]:


billboard_ratings = billboard_ratings[['id','date.entered','week','rating']]


# In[86]:


# Save Dataset
billboard_ratings.to_csv('billboard_ratings.csv', index=False)


# In[87]:


billboard_ratings.info()


# In[88]:


billboard_song.info()


# In[99]:


# Summray

weather_tidy = (weather_melt.pivot_table(
        index=['id','year','month','day'],
        columns='element',
        values='temp'
    
)
                .reset_index()
)


# In[ ]:





# In[96]:


weather_tidy.head()


# In[ ]:




