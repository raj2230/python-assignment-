#!/usr/bin/env python
# coding: utf-8

# In[9]:


surname = input("Enter your surname: ")
given_name = input("Enter your given name: ")


# In[10]:


full_name = given_name + " " + surname
print(full_name)


# In[17]:


short_name = surname[0].upper() + ". " + given_name[0].upper()+""+given_name[1:]
print(short_name)


# In[20]:


given_name_limit = given_name[:15]
print(given_name)


# In[ ]:




