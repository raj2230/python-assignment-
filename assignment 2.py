#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python dictionary methods
#clear,copy,fromkeys,get,items,keys,pop,popitems,setdefault,update,values.


# In[1]:


raj ={"age":20,"year":2003,"place":"Hyderabad"}
raj.clear()
print(raj)


# In[2]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a =raj.copy()
print(a)


# In[3]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a =raj.get("place")
b =raj.get("age")
print(a)
print(b)


# In[4]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a =raj.items()
print(a)


# In[5]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a =raj.keys()
print(a)


# In[6]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
raj.pop("place")
print(raj)


# In[7]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a=raj.popitem()
print(a)


# In[8]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a = raj.setdefault("palce","Chennai")
print(a)


# In[9]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
raj.update({"height":5.9})
print(raj)


# In[10]:


raj={"age":20,"year":2003,"place":"Hyderabad"}
a = raj.values()
print(a)


# In[ ]:




