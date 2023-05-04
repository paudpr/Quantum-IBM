import pandas as pd
import numpy as np
import re

df = pd.read_csv('~/Desktop/42/Quantum-IBM/42AI_engineering/module_00/ex01/appstore_games.csv')

cols_keep = ["ID", "Name", "Average User Rating", "Price", "Description", "Developer", "Age Rating", "Languages", "Size", "Primary Genre", "Genres", "Original Release Date", "Current Version Release Date", "User Rating Count"]
col_list = list(df.columns)
col_list = list(set(col_list).difference(cols_keep))

df.drop(col_list, axis=1, inplace=True)

def df_nan_filter(df):
	df.dropna(subset=["Size"], inplace=True)
	df['Languages'] = df['Languages'].fillna('EN', inplace=True)
	df['Price'] = df['Price'].fillna(0.0, inplace=True)
	med = df['Average User Rating'].median()
	df['Average User Rating'] = df['Average User Rating'].fillna(med, inplace=True)
	df['User Rating Count'] = df['User Rating Count'].fillna(1, inplace=True)

df_nan_filter(df)

def change_date_format(date: str):
	aux = date.split('/')
	return '-'.join(aux[::-1]) 
	
df["Original Release Date"] = df["Original Release Date"].apply(lambda x: change_date_format(x))
df["Current Version Release Date"] = df["Current Version Release Date"].apply(lambda x: change_date_format(x))

def string_filter(s: str):
	s = re.sub(r'''\\+(t|n|U[a-z0-9]{8}|u[a-z0-9]{4}|x[a-z0-9]{2}|[\.]{2})''', ' ', s)
	s = s.replace('\\\'', '\'').replace('\\\\', '\\')
	s = re.sub(r' +', ' ', s)
	return (s)

df["Description"] = df["Description"].apply(lambda x: string_filter(x))
df = df.drop_duplicates(subset='ID')

df['Age Rating'] = df['Age Rating'].apply(lambda x: int(x[:-1]))
df['User Rating Count'] = df['User Rating Count'].apply(lambda x: 0)
df['Size'] = df['Size'].apply(lambda x: int(x))
df = df[df['Name'].str.len() >= 4]

#for e in df:
#    print("'{}' :: {}".format(e, df.loc[0, e]))

df.to_csv('../ex02/appstore_games_cleaned.csv')