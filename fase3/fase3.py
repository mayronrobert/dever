import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

df_suspeitos = pd.read_csv('fase3/suspeitos3.csv', sep='\t')
df_interviews = pd.read_csv('fase3/depoimentos.csv', sep='\t')

resultado = pd.merge(df_suspeitos, df_interviews, left_on='id', right_on='person_id')

assassino_isolado = resultado[resultado['id'] == 8]

print("\n" + "="*95)
print("                          🚨 CULPADO IDENTIFICADO - FASE 3 🚨                          ")
print("="*95)
print(assassino_isolado[['id', 'name', 'address', 'transcript']].to_string(index=False))
print("="*95 + "\n")
print("O culpado foi identificado como thomas brown. A investigação da Fase 3 foi concluída.")