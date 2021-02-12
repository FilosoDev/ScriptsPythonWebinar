# Importa a biblioteca PANDAS
import pandas as pd

# Importa a biblioteca matplotlib
import matplotlib.pyplot as plt

# Essa linha cria um objeto (tipo dataframe) com a planilha do Excel
data = pd.read_excel('Tabela.xlsx') # Precisa existir esse arquivo do Excel em sua máquina

# Lendo o objeto...
print(data)

# Retorna todas as colunas da planilha do EXCEL
print(data.columns)



### Construir gráfico a partir da planilha do Excel
# Seleciona as colunas
data = pd.DataFrame(data,columns=['Ano','IPCA'])

# Plota o gráfico
data.plot(x ='Ano', y='IPCA', kind = 'line')

# Insere título
plt.title("Percentual do IPCA (Inflação) de 2015 a 2020")

# desenha grade no gráfico
plt.grid()

# Mostra o gráfico
plt.show()