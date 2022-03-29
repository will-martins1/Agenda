from fileinput import close
import pickle

def salvar_contatos(lista):
    arquivo = open("contatos.bin", "wb")

    pickle.dump(lista, arquivo)
    
    arquivo.close()

def carregar_contatos():
    lista = []

    try:
        arquivo = open ("contatos.bin", "rb")

        lista = pickle.load(arquivo)
        
        arquivo.close()
    except FileNotFoundError:
        pass    
    
    return lista


def existe_contato(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True

    return False


def adicionar(lista):

    while True:
        email = input("Digite o e-mail do contato: ")

        if not existe_contato(lista, email):
            break
        else:
            print("Esse e-mail ja foi utilizado.")
            print("Por favor, tente um novo e-mail.")

    #nesse passo, o e-mail recebido será único


    contato = {
        "email": email,
        "nome": input("Digite o nome: "),
        "tel": input("Digite o telefone: ")
    }

    lista.append(contato)

    print("O contato foi cadastrado com sucesso!\n".format(contato['nome']))


def alterar(lista):
    print(" == Buscar Contato ==")
    if len(lista) > 0:

        email = input("Digite o e-mail a ser alterado: ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informções seguem abaixo: ")
            for contato in lista:
                if contato ['email'] == email:
                    print("Nome: {}" .format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['tel']))
                    print("=============================================\n")

                    contato['nome'] = input("Digite o novo nome do contato: ")
                    contato['tel'] = input("Digite o novo telefone do contato: ")

                    print("Os dados do contato com email {}, foram alterados com sucesso!".format(contato['email']))
                    break
        else:
            print("Não existe contato cadastrado com o email {}.".format(email))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def excluir(lista):
    print(" == Excluir Contato ==")
    if len(lista) > 0:

        email = input("Digite o e-mail a ser excluído; ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informções seguem abaixo: ")
            for i, contato in enumerate(lista):
                if contato ['email'] == email:
                    print("Nome: {}" .format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['tel']))
                    print("=============================================\n")

                    del lista[i]

                    print("O contato foi apagado com sucesso")
                    break
        else:
            print("Não existe contato cadastrado com o email {}.".format(email))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def buscar(lista):
    print(" == Buscar Contato ==")
    if len(lista) > 0:

        email = input("Digite o e-mail a ser encontrado; ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informções seguem abaixo: ")
            for contato in lista:
                if contato ['email'] == email:
                    print("Nome: {}" .format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['tel']))
                    print("=============================================\n")
                    break
        else:
            print("Não existe contato cadastrado com o email {}.".format(email))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def listar(lista):
    print(" == Listar Contatos ==")
    if len(lista) > 0:
        for i, contato in enumerate (lista):
            print("contato {}:" .format(i+1))
            print("\tNome: {}" .format(contato['nome']))
            print("\tEmail: {}".format(contato['email']))
            print("\tTelefone: {}".format(contato['tel']))
            print("=============================================\n")
            break

        print("Quantidade de contatos: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def principal():

    lista = carregar_contatos() #inicializando a lista vazia


    while True:
        print(" === Agenda Telefônica ===")
        print(" 1 - Adicionar contato")
        print(" 2 - Alterar contato")
        print(" 3 - Excluir contato")
        print(" 4 - Buscar contato")
        print(" 5 - Listar contatos")
        print(" 6 - Sair")
        opção = int(input("> "))

        if opção == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opção == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opção == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opção == 4:
            buscar(lista)
        elif opção == 5:
            listar(lista)
        elif opção == 6:
            print("Saindo do Programa...")
            break
        else:
            print("Opção inválida. Por favor tente novamente.")

principal()