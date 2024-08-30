# Dicionários

'''game = {'nome' : 'Super Mario',
        'desenvolvedora' : 'Nintendo',
        'ano' : 1990}
print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

for keys, values in game.items():
        print(f'{keys} = {values}')
        '''
        
# dicionário dentro de uma lista

'''
game = {}
games = []

for i in range(3):
        game['nome'] = input("Qual o nome do jogo? ")
        game['videogame'] = input("Para qual videogame ele foi lançado? ")
        game['ano'] = input("Qual o ano de lançamento? ")
        games.append(game.copy())
print('-' * 20)
for jogos in games:
        for chave, valor in jogos.items():
                print(f'O campo {chave} tem o valor {valor}')'''
                
                
# Lista dentro de um dicionário

'''games = {'nome':[], 'videogame':[], 'ano':[]}
for i in range(3):
        nome = input('Qual o nome do jogo? ')
        videogame = input('Para qual videogame foi lançado? ')
        ano = input('Qual o ano do lançamento? ')
        games['nome'].append(nome)
        games['videogame'].append(videogame)
        games['ano'].append(ano)
print('-' * 20)
print(games)'''