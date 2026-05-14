import pandas as pd

df = pd.read_csv("detailed_ev_charging_stations.csv")

coluna = "Cost (USD/kWh)"

k = 6

classes = pd.cut(df[coluna], bins=k)

freq_abs = classes.value_counts().sort_index()
freq_rel = (freq_abs / freq_abs.sum()) * 100
freq_acum = freq_abs.cumsum()
freq_rel_acum = freq_rel.cumsum()

tabela_freq = pd.DataFrame({
    "Custo em USD/kwh": freq_abs.index.astype(str),     
    "Frequência Absoluta": freq_abs.values,
    "Frequência Relativa (%)": freq_rel.round(2).values,
    "Frequência Acumulada": freq_acum.values,
    "Frequência Relativa Acumulada (%)": freq_rel_acum.round(2).values
})

print(tabela_freq.to_string(index=False))

# Nota-se grande variação de preços nas recargas, com números de estações extremamente próximos entre as faixas
# Isto sugere que é possível realizar uma diminuição significativa nos preços de diversas estações de recarga, caso haja uma padronização.


coluna2 = "Installation Year"

k = 3

freq_abs = df[coluna2].value_counts().sort_index()
freq_rel = (freq_abs / freq_abs.sum()) * 100
freq_acum = freq_abs.cumsum()
freq_rel_acum = freq_rel.cumsum()

tabela_freq2 = pd.DataFrame({
    "Valor": freq_abs.index,
    "Frequência Absoluta": freq_abs.values,
    "Frequência Relativa (%)": freq_rel.round(2).values,
    "Frequência Acumulada": freq_acum.values,
    "Frequência Relativa Acumulada (%)": freq_rel_acum.round(2).values
})

print(tabela_freq2.to_string(index=False))

# Percebe-se um aumento no número de estações de recarga criadas ao longo dos anos
# Demonstrando a tendencia de aumento no mercado de carros eletricos