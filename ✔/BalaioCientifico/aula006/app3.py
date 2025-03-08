import seaborn as sns
import matplotlib.pyplot as plt

# Carregar um conjunto de dados embutido
data = sns.load_dataset("iris")

# Criar um gráfico de dispersão
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")

plt.show()
