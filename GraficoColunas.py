# Importa a biblioteca matplotlib
import matplotlib.pyplot as plt

# Cria uma lista com os anos correspondentes ao IPCAs 
anos = [2015, 2016, 2017, 2018, 2019, 2020]

# Cria uma lista com os IPCAs (Índice Nacional de Preços ao Consumidor Amplo) 
ipca = [10.67, 6.29, 2.95, 3.75, 4.31, 4.52]

# Constrói o gráfico correlacionando anos x ipca
plt.bar(anos, ipca)

# Determina limites nos eixos y e y
plt.ylim(2015, 2020)
plt.ylim(1, 12)

# Insere rótulos nos eixos x e y
plt.xlabel('Eixo x - Anos de 2010 a 2020')
plt.ylabel('Eixo Y - IPCA')

# Insere o título
plt.title("Percentual do IPCA (Inflação) de 2015 a 2020")

for x, y in zip(anos, ipca):  # percorre cada ponto ipca x ano e monta pares com os valores
    plt.text(x-0.2, y+0.2, y) # adiciona um texto (o valor) em cada ponto ipca x ano

# Mostra o gráfico
plt.show()