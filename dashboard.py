import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

st.header('Bike Sharing Dashboard :sparkles:')
 
def create_byseason_df(df):
    byseason_df = df.groupby(by="season").registered.sum().sort_values(ascending=False).reset_index()
    byseason_df.rename(columns={
        "registered": "registered_count"
    }, inplace=True)
    
    return byseason_df

all_df = pd.read_csv("all_data.csv")

sum_registered = all_df.groupby("season").registered.sum().sort_values(ascending=False).reset_index()
sum_weathersit = all_df.groupby("weather_situation").registered.sum().sort_values(ascending=False).reset_index()

st.subheader('Best & Worst Performing Season')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
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
 
st.pyplot(fig)

st.subheader('Best & Worst Performing Weather Season')

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

st.pyplot(fig)