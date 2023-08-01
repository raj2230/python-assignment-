#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List comprehension with if condition
number_list=[x for x in range(20) if x % 2==0]
print(number_list)


# In[3]:


number_list=[x for x in range(20) if x % 2!=0]
print(number_list)


# In[3]:


# Lambda function
str="welcom to python"
upper = lambda string:str.upper()
print(upper(str))


# In[2]:


max = lambda a,b : a if (a>b) else b
print(max(1,2))


# In[40]:


add = lambda n1,n2 : n1+n2
sub = lambda n1,n2 : n1-n2
print(add(10,20))
print(sub(10,20))


# In[56]:


# using lambda funcation with map().
set1 =(1,2,3,4,5)
y=set(map(lambda x: x+3,lst))
print(y)



# In[61]:


num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = set(map(lambda x, y: x + y, num1, num2))
print(result)


# In[60]:


#using lambda funcation with filter().
ages=(13,12,18,19,20,22,21,25)
adults_ages =set(filter(lambda age:age>18,ages))
print(adults_ages)
              
        


# In[65]:


#using lambda funcation with reduce().
#from functools import reduce
lis=[1,2,3,4,5]
sum=reduce((lambda x,y :x+y),lis)
print(sum)


# In[71]:


#using zip() function.
a=[1,2,3]
b=['x','y','z']
new=zip(a,b)
print(set(new))


# In[ ]:




