#Mensagem de boas-vindas
print("Sejam Bem-vindo a Loja de Gelados do Rafael Nogueira")
print("----------------------Cardápio----------------------")
print("----------------------------------------------------")
print("----|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)  |----")
print("----|     P     |    R$  9.00    |   R$ 11.00  |----")
print("----|     M     |    R$ 14.00    |   R$ 11.00  |----")
print("----|     G     |    R$ 18.00    |   R$ 11.00  |----")
print("----------------------------------------------------")
print("Desenvolvido por Rafael Nogueira")

# Inicialização do acumulador de valores
total_pedido = 0

# Estrutura de repetição
while True:
    # Input do sabor
    sabor = input("Digite o sabor desejado (CP para Cupuaçu ou AC para Açaí): ").upper()
    
    # Verifica se o sabor é válido
    if (sabor != "CP" and sabor != "AC"):
        # Mensagem de erro para sabor inválido
        print("Sabor inválido. Tente novamente.")
        # Retorna ao início do loop
        continue
    
    #Input do tamanho
    tamanho = input("Digite o tamanho desejado (P, M ou G): ").upper()
    
    # Verifica se o tamanho é válido
    if (tamanho != "P" and tamanho != "M" and tamanho != "G"):
        #Mensagem de erro para tamanho inválido
        print("Tamanho inválido. Tente novamente.\n")
        # Retorna ao início do loop
        continue
    
    # Verifica o sabor e o tamanho escolhidos e acumula o valor do pedido
    if (sabor == "CP"):
        if (tamanho == "P"):
            total_pedido += 9
        elif (tamanho == "M"):
            total_pedido += 14
        elif (tamanho == "G"):
            total_pedido += 18
    elif (sabor == "AC"):
        if (tamanho == "P"):
            total_pedido += 11
        elif (tamanho == "M"):
            total_pedido += 16
        elif (tamanho == "G"):
            total_pedido += 20
    
    # Print do valor do pedido atual
    print(f"Pedido: {tamanho} de {sabor} - Valor: R${total_pedido}\n")
    
    # Verifica se o usuário deseja fazer outro pedido
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if (continuar != "S"):
        break

# Saída do valor total do pedido
print(f"\nTotal do pedido: R${total_pedido}")