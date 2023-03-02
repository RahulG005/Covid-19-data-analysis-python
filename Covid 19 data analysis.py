#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\Rahul\OneDrive\Desktop\dataset\4. covid_19_data.csv")


# In[3]:


data.head()


# In[4]:


data.count()


# In[5]:


#show the total null values in each column
data.isnull().sum()


# In[6]:


import seaborn as sns


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


#show null value in heatmap as white space
sns.heatmap(data.isnull())
plt.show


# In[9]:


#show number of confirmed, deaths and recovered case in each region and sort it in descending
data.groupby('Region').sum().sort_values(by = 'Confirmed',ascending = False)


# In[10]:


#Remove the data with less than 10 confirmed cases
data = data[~(data.Confirmed<10)]
data


# In[11]:


#Top 5 regions with high confirmed cases
TOP5 = data.groupby('Region').sum().sort_values(by = 'Confirmed',ascending = False).head(5)
TOP5


# In[12]:


#Plotting top 5 regions
TOP5.plot(kind="bar",width = 0.8)
plt.title("Cases of top 5 Region")


# In[ ]:




