while True:
    nome = input("Qual o seu nome?")
    if (nome != 'Lenhadorzinho'):
        continue #Volta para o início do laço
    senha = input("Qual a sua senha?")
    if (senha == 'UnInTeR'):
        break
    
print("Acesso concedido")