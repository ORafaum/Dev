'''
        Exercício com While

inicial = int(input("Qual valor deseja iniciar a contagem?"))
final = int(input("Qual valor deseja encerrar a contagem?"))

x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1
    '''    
'''
# Exercicio com For

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print(f"A média dos pares de 1 até 100 é: {media}")
'''

#Exercicio com tabuada

for tabuada in range(1,11,1):
    print(f"TABUADA DO {tabuada}")
    for i in range(1,11,1):
        print(f"{tabuada} x {i} = {tabuada * i}")

