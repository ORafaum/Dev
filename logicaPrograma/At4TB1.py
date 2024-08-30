print("Bem vindos ao serviço de cadastro de Livros do Rafael Nogueira")
print('-' * 75)
lista_livro = []
id_global = 0

# Função de cadastrar o Livro
def cadastrar_livro(id):
    print('-' * 10, 'MENU CADASTRAR LIVROS', '-' * 10)
    livro = {}
    livro['id'] = id
    print(f"ID: {id}")
    livro['nome'] = input("Qual o nome do Livro?")
    livro['autor'] = input("Qual o nome do autor(a)? ")
    livro['editora'] = input("Qual é a editora deste livro?")
    #Copio todo o dicionário para dentro da lista lista_livro[]
    lista_livro.append(livro.copy())
    
# Função de consultar os livros
def consultar_livros():
    print('-' * 10, 'MENU CONSULTAR LIVROS', '-' * 10)
    # Enquanto não quebrar o código continua rodando
    while True:
        servico_consulta = input("Qual opção deseja?\n 1. Consultar Todos \n 2. Consultar por ID \n 3. Consultar por autor \n 4. Retornar ao menu\n")
        # Se o input for 1 vai me mostrar todos os itens da lista_livro()
        if (servico_consulta == '1'):
            print('-' * 30)
            for livro in lista_livro:
                 print(f"ID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}\n")
        # Vai me dar a consulta baseada no ID que o usuário insere dentro do input id_consulta
        elif(servico_consulta == '2'):
            id_consulta = int(input("Insira o ID do livro"))
            # Fiz esse código me baseando que como ia ser uma consulta de um único resultado (os id's) usei booleano para que me retornasse apenas o que seria suposto
            livro_encontrado = False
            for livro in lista_livro:
                # Se achar o livro pelo ID vai me trazer a print do livro encontrado
                if livro['id'] == id_consulta:
                    print(f"ID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}\n")
                    # Booleano de livro encontrado é verdadeiro
                    livro_encontrado = True
                    # Retorno ao código principal
                    break
            # Se livro_encontrado for falso vai retornar ao começo do loop e me perguntar o ID novamente
            if not livro_encontrado:
                print("Livro não encontrado")
        # Se servico_consulta = 3 vai me solicitar o input do autor do livro
        elif(servico_consulta == '3'):
            autor_consulta = input("Digite o nome do autor: ")
            # Fiz uma nova lista, inserindo apenas os livros que aquele respectivo autor fez 
            # [livro(Compreensão da lista) for livro in lista_livro, Agora, se o livro['autor].minúsculo for igual ao meu input de autor_consulta] for verdadeiro
            livros_autor = [livro for livro in lista_livro if livro['autor'].lower() == autor_consulta.lower()]
            if livros_autor:
            # Vai me trazer a print dos livros do autor inserido no input
                for livro in livros_autor:
                    print(f"ID: {livro['id']} \nNome: {livro['nome']} \nAutor: {livro['autor']} \nEditora: {livro['editora']}\n")
            else:
                print("Nenhum livro encontrado para este autor.\n")
        # Se 4, vai retornar ao código Principal
        elif (servico_consulta == '4'):
            return
        
# Função de remover o livro
def remover_livro():
    print('-' * 10, 'MENU DE REMOVER LIVROS', '-' * 10)
    while True:
    # Fiz basicamente a mesma coisa que a consulta por ID, porém eu fiz com um resultado diferente, só fiz invés de printar o livro, apenas notificar que o livro foi deletado
        id_remover = int(input("Qual é o id desejado a ser removido?"))
        id_encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                id_encontrado = True
                print("Livro deletado.")
        if not id_encontrado:
            print("Livro não encontrado")
        else:
            return       
# Código Principal com um loop infinito 
while True:  
    # Menu de serviços
    print('-' * 15, "Menu Principal", '-' * 15)
    servico = input("Qual opção deseja escolher?: \n 1. Cadastrar Livro \n 2. Consultar livro \n 3. Remover livro \n 4. Encerrar programa \nOpção: ")
    if (servico == '1'):
        id_global += 1 # Id global + 1 toda vez que eu cadastrar um novo livro
        cadastrar_livro(id_global) # Chama a função com o id_global como parâmetro
    elif(servico == '2'):
        consultar_livros() # Chama a função de consultar os livros
    elif(servico == '3'):
        remover_livro() # Chama a função de remoção de livros
    elif(servico == '4'):
        print("Encerrando programa, obrigado pela visita")
        break
    # Se nenhuma das opções for atendida, vai repetir o código principal
    else:
        print("Opção inválida, por favor tente novamente.\n")