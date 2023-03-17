#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openpyxl


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('zomato.csv', encoding = 'latin-1')
df.head(3)


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe()


# In[19]:


df.shape


# In[7]:


df.isnull().sum()


# In[20]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[72]:


plt.figure(figsize=(12,6))
sns.heatmap(df.isnull(), yticklabels=False, cmap='viridis',cbar=False)


# In[10]:


df_country = pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[11]:


df_country.columns


# In[12]:


final_df = pd.merge(df,df_country,on='Country Code',how='right')


# In[13]:


final_df.head(2)


# In[14]:


final_df.dtypes


# In[21]:


country_names = final_df.Country.value_counts().index
country_names


# In[17]:


country_values = final_df.Country.value_counts().values
country_values


# In[24]:


plt.pie(country_values[:3], labels=country_names[:3], autopct='%1.2f%%');


# In[25]:


city_names = final_df.City.value_counts().index
city_names


# In[27]:


city_values = final_df.City.value_counts().values
city_values


# In[35]:


plt.pie(city_values[:3], labels = city_names[:3],autopct = '%1.2f%%');


# In[49]:


plt.plot(city_names[:5],city_values[:5],'o--r');
plt.bar(city_names[:5],city_values[:5])


# In[58]:


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[61]:


ratings


# In[77]:


plt.figure(figsize=(10,5))
sns.barplot(data=ratings, x='Aggregate rating',y='Rating count',hue='Rating color', palette=['white','red','violet','yellow','green','black']);


# In[82]:


plt.figure(figsize=(10,5))
sns.countplot(data=ratings, x='Rating color',hue='Rating color', palette=['white','red','violet','yellow','green','black']);


# In[91]:


final_df[final_df['Rating color']=='White'].groupby(['Country']).size().reset_index


# In[93]:


final_df.columns


# In[94]:


final_df.head(5)


# In[100]:


final_df.groupby(['Currency','Country']).size().reset_index()


# In[101]:


final_df.columns


# In[109]:


final_df.groupby(['Country','Has Online delivery']).size().reset_index()


# In[ ]:




