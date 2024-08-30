'''
# Funções

def borda(s1):
    tam = len(s1)
    # Só imprime caso exista algum caractere
    if tam:
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+','-' * tam, '+')
        
borda('Olá mundo')
borda('Lógica de programação e algoritmos')'''

# Escopo de variáveis

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam= len(s1)
    while((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = valida_string('Digite uma string:', 10, 20)
print("Você digitou a string {}. \n Dado válido. Encerrando o programa...".format(x))