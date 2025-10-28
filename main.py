import pandas as pd
import numpy as np

df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1, how='all')
print(df.head())
print(df.shape)
print(df.info())

budget_df = df[df['budget']>1000000]
print(budget_df.shape)

budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'] )
print(budget_lookup)
print(budget_lookup[['Jumanji']])

movies_by_runtime = pd.Series(df['title'].values, index=df['runtime'])
movies_by_runtime = movies_by_runtime.sort_index()
print(movies_by_runtime.loc[10:180])

# part D

df_highly_voted = df[df.vote_count > 20]
df_high_rated = df_highly_voted[df_highly_voted.vote_average > 8]
df_high_rated[['title', 'vote_average', 'vote_count']].head()