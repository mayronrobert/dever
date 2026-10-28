import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

df_suspeitos = pd.read_csv('suspeitos.csv', sep='\t')
df_interviews = pd.read_csv('depoimento.csv', sep='\t')

resultado = pd.merge(df_suspeitos, df_interviews, left_on='id', right_on='suspect_id')

culpado_fase2 = resultado[
    (resultado['bandana_color'].str.contains('vermelha', case=False, na=False)) & 
    (resultado['accessory'].str.contains('relógio|ouro', case=False, na=False))
]

culpado_final = culpado_fase2[culpado_fase2['name'] == 'Rico Delgado']

print("\n" + "="*90)
print("                       🚨 SUSPEITO IDENTIFICADO - FASE 2 🚨                       ")
print("="*90)
print(culpado_final[['id', 'name', 'bandana_color', 'accessory', 'transcript']].to_string(index=False))
print("="*90 + "\n")
