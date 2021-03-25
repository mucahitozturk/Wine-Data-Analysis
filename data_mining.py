# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:47:54 2020

@author: Mücahit Öztürk and Beyza Nur Bütün



"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\mucah\Desktop\Data_Mining_Odev\UzumSatisVeriSeti.xlsx')
df.columns=['tarih','ort_satis','top_miktar',
            'yesil','kirmizi','mor','top_kasa','kucuk_kasa',
            'buyuk_kasa','xl_kasa','uretim_tipi','sehir']

df.head()

# IDENTIFYING NUMERICAL FEATURES

numeric_data = df.select_dtypes(include=np.number) # select_dtypes selects data with numeric features
numeric_col = numeric_data.columns      # we will store the numeric features in a variable
print("===="*20)
print("Numeric Features:")
print(numeric_data.head())
print("===="*20)

# IDENTIFYING CATEGORICAL FEATURES
categorical_data = df.select_dtypes(exclude=np.number) # we will exclude data with numeric features
categorical_col = categorical_data.columns      # we will store the categorical features in a variable

print("===="*20)
print("Categorical Features:")
print(categorical_data.head())
print("===="*20)

# CHECK THE NON-NULL COUNT OF ALL COLUMNS:
print(df.info())

# Selecting the categorical columns
categorical_col = df.select_dtypes(include=['object']).columns
plt.style.use('ggplot')
# Plotting a bar chart for each of the cateorical variable
for column in categorical_col:
    plt.figure(figsize=(10,4))
    plt.subplot(121)
    df[column].value_counts().plot(kind='bar')
    plt.title(column)
    
plt.figure(figsize=(12,5))
plt.title("Average selling price distribution (TL)")
ax = sns.distplot(df["ort_satis"], color = 'blue')

df['year']=df['tarih'].dt.year
df['month']=df['tarih'].dt.month
df.set_index('tarih')

dategroup=df.groupby('month').mean()
plt.figure(figsize=(12,5))
dategroup['ort_satis'].plot(x=df.month, color='red')
plt.title('Average selling price by months (TL)')

dategroup=df.groupby('year').mean()
plt.figure(figsize=(12,5))
dategroup['ort_satis'].plot(x=df.year, color='red')
plt.title('Average selling price by years (TL)')

dategroup=df.groupby('tarih').mean()
plt.figure(figsize=(12,5))
dategroup['ort_satis'].plot(x=df.year)
plt.title('Average selling price according to 2015-2018 data (TL)')

dategroup=df.groupby('tarih').mean()
plt.figure(figsize=(12,5))
dategroup['yesil'].plot(x=df.year,color='green')
dategroup['kirmizi'].plot(x=df.year,color='red')
dategroup['mor'].plot(x=df.year,color='purple')
plt.title('Sales amount according to grape types (KG)')

dategroup=df.groupby('year').mean()
plt.figure(figsize=(12,5))
dategroup['top_miktar'].plot(x=df.year)
plt.title('Total amount by years (KG)')

dategroup=df.groupby('month').mean()
plt.figure(figsize=(12,5))
dategroup['top_miktar'].plot(x=df.month)
plt.title('Total amount by month (KG)')

dategroup=df.groupby('tarih').mean()
plt.figure(figsize=(12,5))
dategroup['top_miktar'].plot(x=df.year)
plt.title('Total amount according to 2015-2018 data (KG)')

dategroup=df.groupby('tarih').mean()
plt.figure(figsize=(12,5))
dategroup['kucuk_kasa'].plot(x=df.tarih,color='green')
dategroup['buyuk_kasa'].plot(x=df.tarih,color='red')
dategroup['xl_kasa'].plot(x=df.tarih,color='purple')
plt.title('Box quantities according to box sizes')