import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import seaborn as sns

ibov = yf.download(tickers="^BVSP", start="2020-01-01", end="2025-06-01", interval="1d")
inner = ibov
ibov.columns = [f'{p}_{t}' for p,t in ibov.columns]
with open('acoes_ibov_raw.csv','r') as acoes_ibov_file:
    acoes_ibov = csv.reader(acoes_ibov_file)
    headers = next(acoes_ibov)
    acoes_totais = []
    for row in acoes_ibov:
        row_splited = row[0].split(';')
        indices = []
        indices.append(row_splited[2])
        if len(row)>1:
            for i in range(1, len(row)):
                indices.append(row[i])

        acoes_totais.append([row_splited[0], row_splited[1], indices])
        
acoes_cotadas = []
for acao in acoes_totais:
    if "IBOV" in acao[2]:
        acao_revisada = (acao[1]+".SA").replace(" ","")
        acoes_cotadas.append(acao_revisada)

# acoes_gerais = yf.download(tickers=acoes_cotadas, start="2020-01-01", end="2025-06-01", interval="1d")
ibov_melt = ibov.reset_index().melt(id_vars=["Date"], var_name="var", value_name="val")
print(ibov_melt[ibov_melt["Date"]=='2020-01-02'])
print(ibov_melt.columns)
# inner = inner.join(acoes_gerais, how='inner', lsuffix=f"_IBOV")
# tips = sns.load_dataset("tips")
# sns.set_theme(style="ticks", palette="pastel")
# sns.boxplot(data=ibov_melt[ibov_melt["Date"]<'2020-03-02'], x="Date", y="val")
# sns.despine(offset=10, trim=True)
# plt.show()
# inner.plot(figsize=(14, 7))
# plt.title("IBOV e Ações Cotadas")
# plt.xlabel("Data")
# plt.ylabel("Preço de Fechamento")
# plt.show()