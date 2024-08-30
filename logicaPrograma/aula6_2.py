'''mochila = ['Machado' , 'Camisa', 'Bacon', 'Abacate']
for item in mochila: # Estou acessando o conjunto de strings dentro da lista (Letras são strings)
    for letra in item: # Estou acessando as strings e estou fazendo a iteração com base na quantidade de strings (Letras)
        print(letra, end='')
    print()'''
    
    

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input("Digite a quantidade: ")))
    item.append(float(input("Digite o valor: ")))
    mercado.append(item[:]) # Coloco [:] dentro da lista 'item' pra conseguir copiar a lista de cima # mercado.append(item[:]) para copiar todos os inputs dentro da variável item
    item.clear() # Dou clear nos itens em toda iteração e deixo apenas os valores únicos, porque senão ia criar 3 listas dentro da lista, e com isso eu crio só uma (se quiser testa sem)
print(mercado)

'''mercado = []

for i in range(3):
    nome = input("Digite o nome do item: ")
    qtd = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor: "))
    mercado.append([nome, qtd, valor])
print(mercado)'''