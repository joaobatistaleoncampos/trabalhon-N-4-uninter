# Exigência de código 1 de 8

print("\nBem vindos a lista de contatos joão batista leon campos")
print('-'  *58,)
print( "-" *21,'MENU PRINCIPAL' ,'-'*21,)
print("Escolha a opção desejada:")

# Exigência de código 2 de 8
lista_contatos = []
id_global = 1902942  # Substitua este número pelo seu RU

# Exigência de código 3 de 8
def cadastrar_contato(id):
    id = input("Id do contato:")
    nome = input("Informe o nome do contato: ")
    atividade = input("Informe a atividade do contato: ")
    telefone = input("Informe o telefone do contato: ")
    contato = {
        
         ' id': id ,
         
        ' nome': nome,
        
        ' atividade': atividade,
        
        'telefone': telefone
    }
    lista_contatos.append(contato.copy())

# Exigência de código 4 de 8
def consultar_contatos():
    while True:
        opcao = input("Escolha a opção desejada: \n 1- Consultar Todos os contatos \n 2- Consultar por Id \n 3- Consultar por Atividade \n 4- Retornar ao menu \n >> ")
        if opcao == "1":
            for contato in lista_contatos:
                print(contato)
        elif opcao == "2":
            id_consulta = int(input("Informe o id do contato: "))
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(contato)
                    break
            else:
                print("Contato não encontrado.")
        elif opcao == "3":
            atividade_consulta = (input("Informe a atividade: "))
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(contato)
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")

# Exigência de código 5 de 8
def remover_contato():
    while True:
        id_remove = int(input("Informe o id do contato a ser removido: "))
        for contato in lista_contatos:
            if contato['id'] == id_remove:
                lista_contatos.remove(contato)
                print("Contato removido.")
                return
        print("Id inválido. Tente novamente.")

# Exigência de código 6 de 8
while True:
    print("1) Cadastrar Contato")
    print("2) Consultar Contato (s)")
    print("3) Remover Contato")
    print("4) Sair")
    
    opcao = input(">> ")
    
    if opcao == "1":
        print('-'  *58,)
        print( "-" *17,'MENU CADASTRAR CONTATOS' ,'-'*17,)
        id_global += 1
        cadastrar_contato(id_global)
    elif opcao == "2":
        print('-'  *58,)
        print( "-" *17,'MENU consultar CONTATOS' ,'-'*17,)
        consultar_contatos ( )
        
    elif opcao == "3":
        print('-'  *58,)
        print( "-" *17,'MENU REMOVER CONTATOS' ,'-'*17,)
        remover_contato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Exigências de saída de console e exemplos para testar o programa
# Substitua [Seu Nome Completo] pelo seu nome completo real
# Exemplo de contato: nome completo, atividade como estudante e telefone como seu RU
cadastrar_contato(id_global)
consultar_contatos()
remover_contato()
consultar_contatos()