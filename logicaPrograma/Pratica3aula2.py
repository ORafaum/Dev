kwh = float(input("Quantos kWh?"))
tipo = input("Qual o tipo de instalação? R, C ou I")

if(tipo == 'R'):
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f"Total a pagar: {kwh * preco}")
elif(tipo == 'C'):
    if kwh >= 1000:
        preco = 0.6
    else:
        preco = 0.66
    print(f"Total a pagar: {kwh * preco}")
    
elif(tipo == 'I'):
    if kwh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f"Total a pagar: {kwh * preco}")
else:
    print('Tipo de instalação incorreta')