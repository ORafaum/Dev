# Mensagem de Boas vindas com o meu nome
print("Seja Bem vindo à loja do Rafael Nogueira")

# Inputs que me retornam o valor unitário e a quantidade de produtos.
valorunit = float(input("Digite o valor unitário do produto:"))
quantidadeunit = int(input("Agora digite quantos desse produto você quer levar:"))

# Lógica do desconto (se abaixo de 2500 = 0% de desconto)
totalSemDesconto = valorunit * quantidadeunit
if (totalSemDesconto < 2500):
  desconto = 0
# Entre 2500 e 6000 = 4% de desconto
elif (totalSemDesconto >= 2500 and totalSemDesconto < 6000):
  desconto = 0.04
# Entre 6000 e 10000 = 7% de desconto
elif (totalSemDesconto >= 6000 and totalSemDesconto < 10000):
  desconto = 0.07
# Acima de 10000 = 11% (Feito com a lógica else)
else:
  desconto = 0.11

# Cálculo do desconto da compra
totalComDesconto = totalSemDesconto * (1 - desconto)
  
# Mensangem no Terminal dos valores sem o desconto e com o desconto, incluindo a porcentagem
print("Valor total sem desconto R$ {:.2f}".format(totalSemDesconto))
print("Valor total com desconto de {:.0f}%: R$ {:.2f}".format(desconto * 100, totalComDesconto))

# Se compra acima de 2500 Reais, Mostra mensagem de quantos % de desconto foi obtido (4%,7%,11%)
if (totalSemDesconto >= 2500):
  print("Você recebeu um desconto de {:.0f}% por gastar mais de R$ 2500!".format(desconto * 100))