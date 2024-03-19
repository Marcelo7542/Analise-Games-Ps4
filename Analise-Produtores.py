import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import LabelEncoder
warnings.filterwarnings("ignore")


BaseDados = pd.read_csv("PS4_GamesSales.csv", encoding='latin-1')
Função_label = LabelEncoder()
BaseDados["Producer"] = Função_label.fit_transform(BaseDados['Publisher'])

BaseDados["Genre"] = Função_label.fit_transform(BaseDados['Genre'])

BaseDados["Game"] = Função_label.fit_transform(BaseDados['Game'])

paleta = sns.color_palette('husl', 8)
print(paleta)
plt.figure(figsize=(20,5))
sns.scatterplot(data=BaseDados, x="Producer", y="Global", color=paleta[0])
#sns.scatterplot(data=BaseDados, x="Genre", y="Global", color=paleta[0])
#sns.scatterplot(data=BaseDados, x="Game", y="Global", color=paleta[0])
plt.title("Análise dos produtores de jogos (Milhões)")
plt.show()