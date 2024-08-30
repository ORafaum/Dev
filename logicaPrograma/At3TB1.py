# Função para escolher o serviço DIG - ICO etc..
def escolha_servico(pergunta):
    print("Bem vindos a papelaria do Rafael Nogueira")
    print("Qual o serviço desejado?")
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão Preto e Branco")
    print("FOT - Fotocópia")
    # Input para definir o parâmetro pergunta
    servico = input(pergunta).upper()
    # Define a variável precoservico como global para poder ser usada no main()
    global precoservico
    # Condicionais para o precoservico ter um valor
    if(servico == "DIG"):
        precoservico = 1.10
        print("Você escolheu digitalização")
    elif(servico == "ICO"):
        precoservico = 1.00
        print("Você escolheu Impressão colorida")
    elif(servico == "IPB"):
        precoservico = 0.40
        print("Você escolheu Impressão Preto e Branco")
    elif(servico == "FOT"):
        precoservico = 0.20
        print("Você escolheu Impressão colorida")
        
    # Loop que repete todo o código acima para identificar as opções disponíveis
    while(servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'IPB' and servico != 'FOT'):
        print("Serviço inválido por favor escolha um dos serviços abaixo \n \n")
        print("Qual o serviço desejado?")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(pergunta).upper()
        if(servico == "DIG"):
            precoservico = 1.10
            print("Você escolheu digitalização")
        elif(servico == "ICO"):
            precoservico = 1.00
            print("Você escolheu Impressão colorida")
        elif(servico == "IPB"):
            precoservico = 0.40
            print("Você escolheu Impressão Preto e Branco")
        elif(servico == "FOT"):
            precoservico = 0.20
            print("Você escolheu Impressão colorida")
    # Retorna o loop caso input seja inválido
    return

# Função de número das páginas solicitadas
def num_pagina():
    # Deixo as variáveis abaixo como global para ser usado no main()
    global desconto, numpagina
    # Faço um loop para caso me retorne erro
    while True:
        try:
            numpagina = int(input("Por favor insira a quantidade de páginas: "))
            if (numpagina >= 20000):
                print("O número de páginas excede o limite superior")
                continue
            # Condicionais que retornam desconto baseado na quantidade de páginas
            elif(numpagina < 20):
                desconto = 0
                print("Seu desconto atual é de {:.0f}%".format(desconto * 100))
            elif(numpagina >= 20 and numpagina < 200):
                desconto = 0.15
                print("Seu desconto atual é de {:.0f}%".format(desconto * 100))
            elif(numpagina >= 200 and numpagina < 2000):
                desconto = 0.20
                print("Seu desconto atual é de {:.0f}%".format(desconto * 100))
            elif(numpagina >= 2000 and numpagina < 20000):
                desconto = 0.25
                print("Seu desconto atual é de {:.0f}%".format(desconto * 100))
            # Quebra o código
            break
        # Caso seja um erro de valor (Ex: uma string), retorna ao começo do Loop
        except ValueError:
            print("Valor inserido inválido, por favor insira novamente o valor em forma de número")    

# Função dos serviços adicionais
def servico_extra(servextra):
    print("Deseja adicionar algum serviço?")
    print("1 - Encadernação simples R$ 15.00")
    print("2 - Encadernação Capa Dura R$ 40.00")
    print("0 - Não desejo mais nada")
    # Variável extra como global para ser usado no main()
    global extra
    #Loop para caso o input da opção seja incorreta
    while True:
        try:
            opcao = int(input("Número da opção:"))
            if(opcao == 1):
                extra = 15.00
            elif(opcao == 2):
                extra = 40.00
                # Usei dois breaks para eu não me perder onde eu estava
            elif(opcao == 0):
                break
            break
        except ValueError:
            print("Opção inválida, por favor insira uma opção válida")
 
 
            
# Chama a função dos serviços iniciais no código principal
escolha_servico("")
# Quando termina a função anterior essa se inicia
num_pagina()
# Última Função a ser chamada
servico_extra("")


# (Total do serviço * número de páginas) + o serviço extra
total = ((precoservico * numpagina) + extra)
# Calcula o desconto basicamente Total * porcentagem de desconto
totalcomdesconto = ((precoservico * numpagina) + extra)*(desconto)
# Print mostrando todos os valores nas duas últimas variáveis
print("Total: {:.2f} (serviço: {} * páginas {} + extra {}) e um total com desconto de {:.2f} e um desconto de {:.0f}%".format(total,precoservico,numpagina,extra,total - totalcomdesconto,desconto * 100))