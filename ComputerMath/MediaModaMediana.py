import pandas as pd
x = {'Pesos':[67.8,87.6,54.4,98.6,130.8,142.6,161.6,142.5,158.4]}
p=pd.DataFrame(x)
media=p['Pesos'].mean()
moda=p['Pesos'].mode()
mediana=p['Pesos'].median()
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')