import pandas as pd
import numpy as np

df = pd.read_csv("detailed_ev_charging_stations.csv")

# VARIÁVEL QUANTITATIVA CONTÍNUA

coluna = "Cost (USD/kWh)"

n = len(df[coluna].dropna())
k = int(1 + 3.3 * np.log10(n))

classes = pd.cut(df[coluna], bins=k)

freq_abs = classes.value_counts().sort_index()
freq_rel = (freq_abs / freq_abs.sum()) * 100
freq_acum = freq_abs.cumsum()
freq_rel_acum = freq_rel.cumsum()

tabela_freq = pd.DataFrame({
    "Custo em USD/kwh": freq_abs.index.astype(str),
    "Freq. Absoluta": freq_abs.values,
    "Freq. Relativa (%)": freq_rel.round(2).values,
    "Freq. Acumulada": freq_acum.values,
    "Freq. Relativa Acumulada (%)": freq_rel_acum.round(2).values
})

print("\nTABELA - VARIÁVEL CONTÍNUA")
print(tabela_freq.to_string(index=False))

print("\n# Insight 1: Há distribuição relativamente equilibrada entre as faixas de preço.")
print("# Insight 2: Existe potencial para padronização dos preços das recargas.")

# VARIÁVEL QUANTITATIVA DISCRETA

coluna2 = "Installation Year"

freq_abs = df[coluna2].value_counts().sort_index()
freq_rel = (freq_abs / freq_abs.sum()) * 100
freq_acum = freq_abs.cumsum()
freq_rel_acum = freq_rel.cumsum()

tabela_freq2 = pd.DataFrame({
    "Ano": freq_abs.index,
    "Freq. Absoluta": freq_abs.values,
    "Freq. Relativa (%)": freq_rel.round(2).values,
    "Freq. Acumulada": freq_acum.values,
    "Freq. Relativa Acumulada (%)": freq_rel_acum.round(2).values
})

print("\nTABELA - VARIÁVEL DISCRETA")
print(tabela_freq2.to_string(index=False))

print("\n# Insight 1: O número de estações cresce ao longo dos anos.")
print("# Insight 2: O mercado de veículos elétricos demonstra forte expansão.")