import requests
import time

url = "https://api.franciscosensaulas.com/"

def listar_autores():
    response = requests.get(f"{url}/api/v1/biblioteca/autores")
    dados_json = response.json()

    # \033[1m< ... >\033[0m  = negrito
    dado_string: str = f"\033[1mN° | NOME | NACIONALIDADE | DATA DE NASCIMENTO\033[0m"
    i = 1

    # o append ser para adicianar o elemento na última posição da lista
    for autor in dados_json:
        if i % 2 == 0:
            dado_string = (f"\033[0m {i} | {autor['nome']} | {autor['nacionalidade']} | {autor['dataNascimento']}\033[0m") # \033[0m< ... >\033[0m  = normal
            i = i + 1
        else:
            dado_string = (f"\033[2m {i} | {autor['nome']} | {autor['nacionalidade']} | {autor['dataNascimento']}\033[0m") # \033[0m< ... >\033[0m  = cinza
            i = i + 1
        print(dado_string)

    if response.status_code == 200:
        pass
    else:
        print("Ocorreu um erro ao listar os autores")


def cadastrar_autor():
    nome_autor: str = input("Digite o nome do autor: ")
    nacionalidade_autor: str = input("Digite a nacionalidade do autor: ")
    autor_data_nascimento: str = input("Digite a data de nascimento do autor [1974-07-15]: ")

    dados_autor = {
        'nome': nome_autor, 'nacionalidade': nacionalidade_autor, 'dataNascimento': autor_data_nascimento
    }
    response = requests.post(f"{url}/api/v1/biblioteca/autores", json=dados_autor)
    
    if response.status_code == 201:
        print("Autor cadastrado com sucesso" )
    else:
        print("Ocorre um erro ao cadastrar o autor")


def apagar_autor():
    response = requests.get(f"{url}/api/v1/biblioteca/autores")
    dados_json = response.json()

    autor_escolhido: int = int(input("Digite o número do autor que deseja apagar: "))
    index = dados_json[autor_escolhido - 1]
    id_escolhido = index['id']
    
    response = requests.get(f"{url}/api/v1/biblioteca/autores/{id_escolhido}")
    item = response.json()
    print(f"Autor selecionado: {item['nome']} | {item['nacionalidade']} | {item['dataNascimento']}")
    confirmacao: str = input("Tem certeza que deseja apagar esse item [y/n]: ").lower()

    if confirmacao == "y":
        response = requests.delete(f"{url}/api/v1/biblioteca/autores/{id_escolhido}")
        if response.status_code == 204:
            print("Item apagado com sucesso")
        else:
            print("Ocorreu um erro ao apagar o autor")
    elif confirmacao == "n":
        print("Processo de apagamento foi cancelado")
    else:
        print("Opção inválida")


def editar_autor():
    response = requests.get(f"{url}/api/v1/biblioteca/autores")
    dados_json = response.json()

    autor_escolhido: int = int(input("Digite o número do autor que deseja editar: "))
    index = dados_json[autor_escolhido - 1]
    id_escolhido = index['id']

    response = requests.get(f"{url}/api/v1/biblioteca/autores/{id_escolhido}")
    item = response.json()
    print(f"Autor selecionado: {item['nome']} | {item['nacionalidade']} | {item['dataNascimento']}")

    novo_nome_autor: str = input("Digite o nome do autor: ")
    novo_nacionalidade_autor: str = input("Digite a nacionalidade do autor: ")
    novo_autor_data_nascimento: str = input("Digite a data de nascimento do autor [1974-07-15]: ")

    novo_dados_autor = {
        'nome': novo_nome_autor, 'nacionalidade': novo_nacionalidade_autor, 'dataNascimento': novo_autor_data_nascimento
    }

    response = requests.put(f"{url}/api/v1/biblioteca/autores/{id_escolhido}", json=novo_dados_autor)
    if response.status_code == 204:
        print("Autor editado com sucesso" )
    else:
        print("Ocorre um erro ao editar o autor")
    


escolha = -1
while escolha != 0:
    time.sleep(1)
    print(f"\033[1mAPI BIBLIOTECA AUTORES\033[0m\n1 - Listar autores\n2 - Cadastrar autor\n3 - Apagar autor\n4 - Editar autor\n0 - Sair")
    escolha: int = int(input("Digite sua escolha: "))
    if escolha == 1:
        listar_autores()
    elif escolha == 2:
        cadastrar_autor()
    elif escolha == 3:
        apagar_autor()
    elif escolha == 4:
        editar_autor()
    elif escolha == 0:
        print("Sistema encerrado")
    else:
        print("Opção inválida")
