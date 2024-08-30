'''
 Usando Tupla (Lista imutável) em um loop (print de todos os itens na mochila)
mochila = ('Machado', 'Camiseta', 'Bacon', 'Abacate')

for item in mochila:
    print(f"Você possui {item}")'''
    
'''
Fazendo soma de vários números com uma Tupla
def soma(*num):
    acumulador = 0
    print(f"Tupla: {num}")
    for numeros in num:
        acumulador += numeros
    return acumulador


print(f"Resultado: {soma(1,2,3,4,5,6,7,8,9)}\n")'''


# Lista
mochila = ('Machado', 'Camiseta', 'Bacon', 'Abacate')
print('Tupla: ', mochila)

mochila = ['Machado', 'Camiseta', 'Bacon', 'Abacate']
print("Lista: ", mochila)

#Adiciono à última posição
mochila.append('Ovos')
print("Lista: ", mochila)

# Adiciono à uma posição selecionada
mochila.insert(1,'Canivete')
print("Lista: ", mochila)

# Deleto um item de um índice informado (Canivete)
del mochila[1]
print("Lista: ", mochila)

# Deleto um item pelo nome informado (Ovos)
mochila.remove("Ovos")
print("Lista: ", mochila)