#!/usr/bin/env python
# coding: utf-8

# In[4]:


import word_count

input_string = "Hello, programmer! Is python easy to learn?"
str2 = word_count.remove_punc(input_string)
L1 = word_count.word_split(str2)
d1 = word_count.word_dict(L1)
df = word_count.word_freq_table(d1)

print(df)


# In[5]:


import word_count
input_string = "Hello, programmer! Is python easy to learn?"
str2 = word_count.remove_punc(input_string)
L1 = word_count.word_split(str2)
d1 = word_count.word_dict(L1)
df = word_count.word_freq_table(d1)
print(df)


# In[ ]:




