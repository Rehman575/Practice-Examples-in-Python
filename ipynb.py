#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# '''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

# Request input from user
name = input("Enter your Name: ")
age = int(input("Enter Your age: "))

number = int(input('Please enter an additional number:'))

# Evaluate input
year = (100 - age) + 2020

print (('Dear Mr/Ms ' + name + ', you will turn 100 years old on ' + str (year) + '\n' ) * number)


# In[ ]:




