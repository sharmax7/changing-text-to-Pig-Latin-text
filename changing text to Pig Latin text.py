#!/usr/bin/env python
# coding: utf-8

# In[2]:


""""Question: Pig Latin
You are given a piece of English text on a single line. Write a program that translates
the text to Pig Latin. English is translated to Pig Latin by taking the first letter of
every word, moving it to the end of the word, and adding “ay.”
Assumptions
1. All letters are lowercase
2. Each word is separated by a single space
3. Numbers remain unchanged
4. There are no punctuation marks to worry about
Example
Input:
“the 2 quick brown foxes”
Output:
“hetay 2 uickqay rownbay oxesfay”
"""

input = 'the 2 quick brown foxes'
#splitting the strings to form a word list
splitted=input.split(" ")
#changing str 2 in to int 2
splitted[1]=int(splitted[1])
#creating a empty list where all the Pig Latin will be appended
output = []
#using for loop to append letters and numers seperately
for items in splitted:
    if items not in range(0,10):
        pig_latin=items[1:]+items[0]+'ay'
        output.append(pig_latin)
    else:
        output.append(items)
             
output   

