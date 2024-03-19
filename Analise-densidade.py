import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

BaseDados = pd.read_csv("PS4_GamesSales.csv", encoding='latin-1')


plt.figure(figsize=(14,5))

plt.style.use("ggplot")
plt.title("Distribuição das Vendas Globais")
sns.kdeplot(BaseDados["Global"], shade=True, color="green")
plt.show( )