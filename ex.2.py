#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import string
news_article = "The festival that I like the most is Diwali. We celebrate it either in October or in November. In Gujarat, it is celebrated for five days. Every house is decorated with rangoli and oil lamps. We start preparing for Diwali a few weeks in advance by cleaning our houses. Sweets and savouries are made and new clothes are bought for everyone. We celebrate it with a lot of pomp and festivity. I love Diwali because we enjoy bursting crackers, visiting our relatives and having lots of fun with our near and dear ones.The festival that I like the most is Diwali. We celebrate it either in October or in November. In Gujarat, it is celebrated for five days. Every house is decorated with rangoli and oil lamps. We start preparing for Diwali a few weeks in advance by cleaning our houses. Sweets and savouries are made and new clothes are bought for everyone. We celebrate it with a lot of pomp and festivity. I love Diwali because we enjoy bursting crackers, visiting our relatives and having lots of fun with our near and dear ones."
translator = str.maketrans('', '', string.punctuation)
str1 = news_article.translate(translator)
print("str1:", str1)


# In[5]:


L1 = str1.split()
print("L1:", L1)


# In[15]:


d1 = {}
for word in L1:
    if word not in d1:
        d1[word] = 1
    else:
        d1[word] += 1
print("d1:", d1)


# In[17]:


df = pd.DataFrame({"word": list(d1.keys()), "No of occurrences": list(d1.values())})
print(df)


# In[ ]:




