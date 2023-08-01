#!/usr/bin/env python
# coding: utf-8

# In[26]:


import string
def remove_punc(str1):
    translator = str.maketrans('', '', string.punctuation)
    str2 = str1.translate(translator)
    return str2
input_string ="Hello, programmer! Is python easy to learn?"
result = remove_punc(input_string)
print(result)


# In[27]:


def word_split(str2):
    L1 = str2.split()
    return L1
input_string ="Hello programmer Is python easy to learn"
result =word_split(input_string)
print(result)


# In[28]:


def word_dict(L1):
    d1 = {}
    for word in L1:
        d1[word]=d1.get(word,0)+1
    return d1
input_list =['Hello', 'programmer', 'Is', 'python', 'easy', 'to', 'learn']
result =word_dict(input_list)
print(result)


# In[29]:


import pandas as pd
def word_freq_table(d1):
    df = pd.DataFrame(d1.items(), columns=['word', 'No of occurrences'])
    return df
input_dict = {'Hello': 1, 'programmer': 1, 'Is': 1, 'python': 1, 'easy': 1, 'to': 1, 'learn': 1}
result_df = word_freq_table(input_dict)
print(result_df)


# In[33]:





# In[ ]:




