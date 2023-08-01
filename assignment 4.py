#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[32]:


# Create a DataFrame with your subject marks
data = {
    'Subject_name': ['Maths','English','Computer Networks','physics'],
    'Subdivision': ['Communication','Communication','Communication','Communication'],
    'Year': [2023, 2023, 2023,2023],
    'Semester': [1, 1, 1,1],
    'Marks_scored': [90,95,85,80],
    'Max_marks': [100, 100, 100,100],
    'Grade': ['A', 'A', 'B','B']
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)


# In[33]:


#Calculate yearwise average score
yearwise_avg = df.groupby('Year')['Marks_scored'].mean()
print("Yearwise Average Score:")
print(yearwise_avg)


# In[34]:


#Calculate semester wise average score
semesterwise_avg = df.groupby('Semester')['Marks_scored'].mean()
print("Semester Wise Average Score:")
print(semesterwise_avg)


# In[35]:


# Calculate subdivision wise average score
subdivisionwise_avg = df.groupby('Subdivision')['Marks_scored'].mean()
print("Subdivision Wise Average Score:")
print(subdivisionwise_avg)


# In[36]:


#Display the subject scores grade wise
grade_wise_scores = df.groupby('Grade')['Subject_name', 'Marks_scored'].apply(lambda x: x.reset_index(drop=True))
print(grade_wise_scores)


# In[37]:


#categorizing subject marks into as excellent,verygood,good and average.
#funcation to categorize the subject marks
def categorize_marks(marks):
    if marks >=95:
        return 'Excellent'
    elif marks >=90:
        return 'very good'
    elif marks >=85:
        return 'Good'
    else:
        return 'Average'

df['Marks_category'] = df['Marks_scored'].apply(categorize_marks)
print(df)


# In[38]:


df=pd.DataFrame(data)
print(df)


# In[39]:


#calculate mean, median, and standard deviation of Marks_scored
semester_stats = df.groupby('Semester')['Marks_scored'].agg(['mean', 'median', 'std'])
print(semester_stats)


# In[40]:


semester_avg_marks = df.groupby('Semester')['Marks_scored'].mean()

# Create a line plot
plt.plot(semester_avg_marks.index, semester_avg_marks.values, marker='o')

# Set plot labels and title
plt.xlabel('Semester')
plt.ylabel('Average Marks')
plt.title('Semester-wise Average Marks')

# Display the plot
plt.show()


# In[42]:


#Create a bar chart
semester_avg = df.groupby('Semester')['Marks_scored'].mean()
plt.bar(semester_avg.index, semester_avg.values)
plt.xlabel('Semester')
plt.ylabel('Average Marks')
plt.title('Semester-wise Average Marks')
plt.show()


# In[43]:


# Plot a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Marks_scored'], bins=10, edgecolor='black')
plt.xlabel('Marks Scored')
plt.ylabel('Frequency')
plt.title('Histogram of Marks Scored')

# Display the histogram
plt.show()

# Plot a box plot
plt.figure(figsize=(6, 6))
plt.boxplot(df['Marks_scored'])
plt.ylabel('Marks Scored')
plt.title('Box Plot of Marks Scored')

# Display the box plot
plt.show()


# In[ ]:




