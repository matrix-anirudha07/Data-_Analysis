#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None


# In[4]:


df_train = pd.read_csv('train.csv')


# In[5]:


df_train.head(10)


# In[6]:


df_test = pd.read_csv('test.csv')
df_test.head(10)


# In[7]:


df = df_train.append(df_test)
df.head(5)


# In[8]:


df.columns


# In[9]:


df.shape


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


df['Age'].unique()


# In[13]:


df['Age'] = df['Age'].str.replace("+"," ")


# In[14]:


df['Age'].unique()


# In[15]:


df['Age'] = df['Age'].map({'0-17':0, '55 ':6, '26-35':2, '46-50':4, '51-55':5, '36-45':3, '18-25':1})


# In[16]:


df['Age'].head()


# In[17]:


df["Age"]


# In[19]:


df_city=pd.get_dummies(df['City_Category'], drop_first=True)


# In[20]:


df_city.head()


# In[21]:


df= pd.concat([df,df_city], axis=1)


# In[22]:


df.head()


# In[23]:


df.drop(['City_Category'], axis=1,inplace = True)


# In[24]:


df.head()


# In[25]:


df.isnull().sum()


# In[26]:


df['Product_Category_2'].unique()


# In[27]:


df['Product_Category_2'].value_counts()


# In[28]:


df['Product_Category_2'].mode()[0]


# In[29]:


df['Product_Category_2'] = df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])


# In[30]:


df['Product_Category_2'].isnull().sum()


# In[31]:


df['Product_Category_3'].unique()


# In[32]:


df['Product_Category_3'].value_counts()


# In[33]:


df['Product_Category_3'] = df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


# In[34]:


df['Product_Category_3'].mode()


# In[35]:


df['Product_Category_3'].isnull().sum()


# In[36]:


df.head()


# In[37]:


df['Stay_In_Current_City_Years'].unique()


# In[38]:


df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].str.replace('+','');


# In[39]:


df.head()


# In[40]:


df.info()


# In[41]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)
df.info()


# In[42]:


df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)


# In[43]:


df.info()


# In[ ]:




