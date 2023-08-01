#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#append, copy, clear, count, extend, index, insert, pop, remove, reverse, sort, min, max.


# In[1]:


#append=used for adding elements to end of the list.
my_list = [1,2,3,4,5,6,6,7]
my_list.append('numbers')
print(my_list)


# In[1]:


#copy-it used for returns copy of list elements
list =[1,2,3,4,5]
a=list.copy()
print(a)


# In[6]:


#clear is used for the clear the elements prints the empty list
my_list=[1,2,3,4,5,6,6]
#my_list.clear()
my_list.count(6)
#print(my_list)


# In[5]:


list=['apple','orange','Leamon','apple','apple']
list.count('apple')


# In[14]:


list=['apple','orange','Leamon','apple','apple']
more_list=['grape','cherry']
list.extend(more_list)
print(list)


# In[16]:


list=['apple','orange','Leamon','apple','apple']
print(list.index('Leamon'))


# In[19]:


list=['apple','orange','Leamon','apple','apple']
list.insert(2,"rajkumar")
print(list)


# In[21]:


list=[1,2,3,4,5,6]
print(list.pop(5))
print("new list",list)


# In[22]:


list=[1,2,3,4,5,6]
list.remove(4)
print(list)


# In[23]:


list=[1,2,3,4,5,6]
list.reverse()
print(list)


# In[28]:


list=[3,5,4,1,2,6]
list.sort()
print(list)
list.sort(reverse=True)
print(list)


# In[ ]:





# In[30]:


list=[1,2,3,4,5,6]
print(min(list))
print(max(list))


# In[13]:


s1={"python"}
s1


# In[ ]:




