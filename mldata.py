#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Model to Predict Age based on height and weight

# In[2]:


# Install Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# # Load Data Set

# In[5]:


df = pd.read_csv('./mldata.csv')
df.head()


# In[16]:


# Leave Catogrical Data so We can predict on integer values

new_df = df[['age','weight','height']]
new_df.head()


# In[17]:


x = new_df.iloc[:, :-1].values    # Get a copy of Dataset exclude last column
y = new_df.iloc[:, 1].values      # Get a array of dataset in column 1st


# In[18]:


X_train, X_test, y_train, y_test = train_test_split(x , y , test_size=1/3, random_state=0)


# In[19]:


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(X_train, y_train)


# In[20]:


# Predicting the Test set result
y_pred = regressor.predict(X_test)


# In[21]:


y_pred


# In[ ]:




