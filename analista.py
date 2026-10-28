import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df_suspeitos = pd.read_csv('suspeitos.csv', sep='\t')
df_interviews = pd.read_csv('depoimentos.csv', sep='\t')

resultado = pd.merge(df_suspeitos, df_interviews, left_on='id', right_on='suspect_id')

culpado = resultado[resultado['transcript'].str.contains('roubar', case=False, na=False)]

print(culpado[['id', 'name', 'attire', 'transcript']])

