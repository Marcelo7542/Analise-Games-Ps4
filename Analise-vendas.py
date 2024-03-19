import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

BaseDados = pd.read_csv("PS4_GamesSales.csv", encoding='latin-1')

#print(BaseDados.head())
#print(BaseDados.describe())
#print(BaseDados.isnull().sum())
#print(BaseDados.groupby(by=["Year"]).sum())

plt.figure(figsize=(14,5))

sns.barplot(data=BaseDados,x='Year', y="Global", ci=None, estimator=sum)
plt.title("Vendas Globais")
plt.ylabel("Quantidades de vendas")
plt.xlabel("Ano")
BaseDados.loc[(BaseDados["Year"] != 2019) & (BaseDados["Year"] != 2020)]
plt.show( )

