#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: Bike Sharing Dataset
# - Nama:Rahmad Rudiansyah Siregar
# - Email:rrudiansyahsiregar@gmail.com
# - Id Dicoding:rrudiansyah

# ## Menentukan Pertanyaan Bisnis

# - Pada musim apa penyewaan sepada paling banyak?
# - Bagaimana pengaruh cuaca pada penyewaan sepeda ?

# ## Menyiapkan semua library yang dibutuhkan

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## Data Wrangling

# ### Gathering Data

# In[6]:


#Mengambil data set dan menampilkannya


# In[7]:


day_df = pd.read_csv("data/day.csv")
day_df.head()


# ### Assessing Data

# In[8]:


# Memeriksa data missing value
day_df.isnull().sum()


# In[9]:


# Memeriksa duplikat data
day_df.duplicated().sum()


# In[10]:


# melihat informasi mengenai dataset
day_df.info()


# ### Cleaning Data

# In[11]:


# menghapus kolom instant dan dteday karena tidak diperlukan
day_df.drop(['instant','dteday'], axis=1, inplace=True)
day_df.head()


# In[12]:


# menghapus kolom holiday karena sudah terdapat pada kolom workingday
day_df.drop(['holiday'], axis=1, inplace=True)
day_df.head()


# In[13]:


# mengganti nama kolom agar lebih mudah dibaca
day_df.rename(columns={'yr':'year','mnth':'month','weekday':'week_day','workingday':'working_day',
                      'weathersit':'weather_situation','atemp':'temp_feel','hum':'humidity','windspeed':'wind_speed',
                      'cnt':'count'}, inplace=True)


# In[14]:


day_df.head()


# ## Exploratory Data Analysis (EDA)

# ### Explore ...

# In[15]:


# Melihat rangkuman parameter statistik
day_df.describe()


# In[16]:


bike_sharing_df = day_df.copy(deep=True)


# In[17]:


bike_sharing_df.season.value_counts()


# In[18]:


# Membuat penamaan pada kolom season
season_code = {1:'spring', 2:'summer', 3:'fall', 4:'winter'}
bike_sharing_df['season'] = bike_sharing_df['season'].map(season_code)


# In[19]:


bike_sharing_df.season.value_counts()


# In[20]:


bike_sharing_df.weather_situation.value_counts()


# In[21]:


# Membuat penamaan pada kolom weather_situation
weathersit_code = {1:'Clear', 2:'Mist', 3:'Light Snow'}
bike_sharing_df['weather_situation'] = bike_sharing_df['weather_situation'].map(weathersit_code)


# In[22]:


bike_sharing_df.weather_situation.value_counts()


# In[23]:


bike_sharing_df.working_day.value_counts()


# In[24]:


# Membuat penamaan pada kolom working_day
workingday_code = {1:'working_day', 0:'holiday'}
bike_sharing_df['working_day'] = bike_sharing_df['working_day'].map(workingday_code)


# In[25]:


bike_sharing_df.working_day.value_counts()


# In[26]:


bike_sharing_df.month.value_counts()


# In[27]:


# Mengganti nama kode pada kolom month
month_code = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'Mei',6:'Jun',
             7:'Jul',8:'Agt',9:'Sept',10:'Okt',11:'Nov',12:'Des'}
bike_sharing_df['month']=bike_sharing_df['month'].map(month_code)


# In[28]:


bike_sharing_df.month.value_counts()


# In[29]:


bike_sharing_df.week_day.value_counts()


# In[30]:


# Mengganti nama kode pada kolom week_day
weekday_code = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
bike_sharing_df['week_day'] = bike_sharing_df['week_day'].map(weekday_code)


# In[31]:


bike_sharing_df.week_day.value_counts()


# In[32]:


bike_sharing_df.year.value_counts()


# In[33]:


year_code = {0:'2011',1:'2012'}
bike_sharing_df['year'] = bike_sharing_df['year'].map(year_code)


# In[34]:


bike_sharing_df.year.value_counts()


# In[35]:


bike_sharing_df.head()


# In[36]:


bike_sharing_df.groupby(by="season").agg({
    'registered':['mean','max','min']
})


# In[37]:


bike_sharing_df.groupby(by="week_day").agg({
    'registered':['mean','max','min']
})


# In[38]:


bike_sharing_df.groupby(by="working_day").agg({
    'registered':['mean','max','min']
})


# 
# 
# ## Visualization & Explanatory Analysis

#    ### Pertanyaan 1: Pada Season Apa sepeda paling banyak dan paling sedikit disewa ?

# In[39]:


sum_registered = bike_sharing_df.groupby("season").registered.sum().sort_values(ascending=False).reset_index()


# In[40]:


sum_registered.head()


# In[41]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="registered", y="season", data=sum_registered.head(), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Season Paling Banyak Registered", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)
 
sns.barplot(x="registered", y="season", data=sum_registered.sort_values(by="registered", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Season Paling Sedikit Registered", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Best and Worst Season", fontsize=20)
plt.show()


# ### Pertanyaan 2: Bagaimana pengaruh cuaca/weather_situation dalam penyewaan sepeda ?

# In[42]:


sum_weathersit = bike_sharing_df.groupby("weather_situation").registered.sum().sort_values(ascending=False).reset_index()


# In[43]:


sum_weathersit.head()


# In[44]:


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
 
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="registered", y="weather_situation", data=sum_weathersit.head(), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Situasi Cuaca Paling Banyak Registered", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)
 
sns.barplot(x="registered", y="weather_situation", data=sum_weathersit.sort_values(by="registered", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Situasi Cuaca Sedikit Registered", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Best and Worst Weather Situation", fontsize=20)
plt.show()


# ## Conclusion

# - Conclution pertanyaan 1 : dapat dilihat pada EDA dan Visualisasi pelanggan yang melakukan registrasi penyewaan sepeda paling banyak dilakukan pada musim gugur / fall sehingga pada musim ini operator dapat lebih mempersiapkan ketersediaan sepeda agar pelanggan dapat terlayani dengan baik.
# - conclution pertanyaan 2 : dapat dilihat pada EDA dan visualisasi cuaca sangat berpengaruh dalam penyewaan sepeda dimana pada cuaca light snow atau salju sangat sedikit pelanggan yang melakukan registrasi pada musim tersebut.

# In[45]:


# bike_sharing_df.to_csv("all_data.csv", index=False)


# In[ ]:




