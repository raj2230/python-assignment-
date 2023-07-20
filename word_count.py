#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import pandas as pd
def remove_punc(str1):
    translator = str.maketrans('', '', string.punctuation)
    str2 = str1.translate(translator)
    return str2

def word_split(str2):
    L1 = str2.split()
    return L1

def word_dict(L1):
    d1 = {}
    for word in L1:
        d1[word]=d1.get(word,0)+1
    return d1

def word_freq_table(d1):
    df = pd.DataFrame(d1.items(), columns=['word', 'No of occurrences'])
    return df


# In[ ]:




