# Importa a biblioteca matplotlib
import matplotlib.pyplot as plt

# Cria uma lista de frutas
frutas = 'Melancia', 'Maçã', 'Banana', 'Uva'

# Cria uma lista de valores correspondentes a cada fruta
quantidade = [24, 28, 40, 25]

# Quando tem valor acima de 0, destaca a parte correspondente
explode = (0, 0, 0.2, 0)

# Nessa linha a função plt.subplots retorna uma tupla 
# que é desacoplada nas variáveis fig1 e ax1 
fig1, ax1 = plt.subplots()

# Construção da pizza: 
# shadow (sombra)
# startangle (ponto de partida sentido anti-horário)
# autopct determina a formatação (casas decimais e simbolo de porcentagem) dos valores
ax1.pie(quantidade, labels=frutas, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90)

# possibilita um círculo desenhado com proporções iguais (equal)
ax1.axis('equal')

# Insere título
plt.title("Percentual da preferência pelas frutas")

# Mostra o gráfico
plt.show()