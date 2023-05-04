import pandas as pd
import numpy as np
import re

df_orig = pd.read_csv('appstore_games_cleaned.csv')
df = df_orig.drop(['ID', 'Primary Genre', 'Genres', 'Languages'], axis=1)
df_genres = df_orig[['ID', 'Primary Genre', 'Genres']].copy()
df_languages = df_orig[['ID', 'Languages']].copy()

print(df_languages.head())