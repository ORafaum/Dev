'''
# Calcular a média de uma lista
notas = [9,7,7,10,3,9,6,6,2]

print(sum(notas) / len(notas))
'''

# Exercício 1 - Tupla com 5 palavras. Print na tela com as respectivas globais das 10 palavras

palavras = ('Mario' , 'Luigi' , 'Peach' , 'Yoshi' , 'Toad')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=" ")
