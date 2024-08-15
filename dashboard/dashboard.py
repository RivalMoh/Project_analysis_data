import os
os.system('pip install pandas numpy matplotlib streamlit babel seaborn')

import pandas as pd
import matplotlib
#import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')



def monthly_rental(df):
    month_df = df.groupby(by=['year', 'month_name', 'mnth']).cnt.sum().reset_index()
    month_df = month_df.sort_values(by=['year', 'mnth'])
    plot_2011 = month_df[month_df['year'] == 2011]
    plot_2012 = month_df[month_df['year'] == 2012]

    return plot_2011, plot_2012


def season(df):
    season_df = df.groupby(by=['year', 'musim']).cnt.sum().reset_index()
    season_2011_df = season_df[season_df['year'] == 2011]
    season_2012_df = season_df[season_df['year'] == 2012]

    return season_2011_df, season_2012_df


df = pd.read_csv(r"/workspaces/Project_analysis_data/final_data.csv")

df['dteday'] = pd.to_datetime(df['dteday'])

min_date = df['dteday'].min()
max_date = df['dteday'].max()

with st.sidebar:

    # Mengambil start_date dan end_date
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Mengaplikasikan filter ke data yang ada 
filter_df = df[(df['dteday'] >= str(start_date)) & (df['dteday'] <= str(end_date))]

plot_2011, plot_2012 = monthly_rental(filter_df)
season_2011, season_2012 = season(filter_df)

# Membuat header dashboard
st.header('Bike Rental Dashboard :bike:')

st.subheader('Daily Rental')

col1, col2, col3 = st.columns(3)

with col1:
    total_umum = filter_df.casual.sum()
    st.metric('Casual', value=total_umum)

with col2:
    total_registered = filter_df.registered.sum()
    st.metric('Registered', value=total_registered)

with col3:
    total_rental = filter_df.cnt.sum()
    st.metric("Total Rental", value=total_rental)

# Chart jumlah peminjam umum dan berlangganan
casual_sum = filter_df['casual'].sum()
registered_sum = filter_df['registered'].sum()

sizes = [casual_sum, registered_sum]

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(sizes, labels=['Umum', 'Berlangganan'], colors=['gray', 'orange'], autopct='%1.1f%%', startangle=140)
ax.axis('equal')
ax.set_title('Perbandingan Jumlah Penyewa Umum dan Berlangganan')

st.pyplot(fig)

# Chart jumlah penyewa sepeda pada tahun 2011 dan 2012
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(plot_2011['month_name'], plot_2011['cnt'], label='2011', marker='o')
ax.plot(plot_2012['month_name'], plot_2012['cnt'], label='2012', marker='s')

ax.set_title('Jumlah Penyewa Sepeda pada Tahun 2011 dan 2012')
ax.set_xlabel('Month')
ax.set_ylabel('Total')
ax.legend()

fig.tight_layout()
st.pyplot(fig)

# Chart perbandingan jumlah perental sepeda pada setiap season
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(season_2011['musim'], season_2011['cnt'], label='2011', marker='o')
ax.plot(season_2012['musim'], season_2012['cnt'], label='2012', marker='s')

ax.set_title('Jumlah Peminjam Setiap Season pada Tahun 2011 dan 2012')
ax.set_xlabel('Season')
ax.set_ylabel('Total')
ax.legend()

fig.tight_layout()
st.pyplot(fig)
