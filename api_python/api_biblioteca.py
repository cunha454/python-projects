import os
import time
import requests
import questionary
import datetime
from rich import box
from rich.table import Table
from rich.console import Console
from questionary import Style

custom_style_fancy = Style([
    ('qmark', 'fg:#660000 bold'),    
    ('question', 'bold'),          
    ('answer', 'fg:#660000 bold'),
    ('highlighted', 'fg:#660000 bold'),
    ('selected', 'fg:#660000'),
])
console = Console()

url = "https://api.franciscosensaulas.com/api/v1/biblioteca"


def listar_bibliotecas():
    response = requests.get(url)
    dados_json = response.json()
    i = 1
    tabela = Table(title="Bibliotecas cadastradas",show_lines=True,box=box.SQUARE_DOUBLE_HEAD,title_style="reverse")

    tabela.add_column("N°", justify="left", style="#243010")
    tabela.add_column("Nome", justify="left", style="#EECF6D")
    tabela.add_column("Endereço", justify="left", style="#C9ADA7")
    tabela.add_column("Cidade", justify="left", style="#5C677D")
    tabela.add_column("Estado", justify="center", style="#415A77")
    tabela.add_column("CEP", justify="center", style="#6C757D")
    tabela.add_column("Telefone", justify="left", style="#4F772D")
    tabela.add_column("E-mail", justify="left", style="#1D3557")
    tabela.add_column("Website", justify="left", style="#457B9D")
    tabela.add_column("Horário Atendimento", justify="left", style="#720E07")
    tabela.add_column("Data Criação", justify="left", style="#8D99AE")

    for biblioteca in dados_json:
        tabela.add_row(
            str(i),biblioteca["nome"],biblioteca["endereco"],biblioteca["cidade"],biblioteca["estado"],biblioteca["cep"],biblioteca["telefone"],biblioteca["email"],biblioteca["website"],biblioteca["horarioAtendimento"],biblioteca["dataCriacao"])
        i += 1
    console.print(tabela)
    questionary.press_any_key_to_continue("Pressione qualquer botão para continuar").ask()
    chamar_menu()


def cadastrar_biblioteca():
    dados_biblioteca = preencher_dados_biblioteca()

    response = requests.post(url, json=dados_biblioteca)
    if response.status_code == 201:
      questionary.print("Biblioteca cadastrada com sucesso", style="bold fg:darkgreen")
    else:
        questionary.print("Ocorreu um erro ao cadastrar a biblioteca", style="bold fg:darkred")

    questionary.press_any_key_to_continue("Pressione qualquer botão para continuar").ask()
    chamar_menu()


def apagar_biblioteca():
    indice = int(questionary.text("Digite o nº da biblioteca que deseja apagar:").ask()) - 1
    id_escolhido = obter_id_biblioteca(indice)

    response = requests.get(f"{url}/{id_escolhido}")
    biblioteca_escolhida = response.json()

    confirmacao: bool = bool(questionary.confirm("Tem certeza que deseja apagar essa biblioteca:").ask())
    if confirmacao == True:
        response = requests.delete(f"{url}/{biblioteca_escolhida['id']}")
        if response.status_code == 204:
            questionary.print("Biblioteca apagada com sucesso", style="bold fg:darkgreen")
        else:
            questionary.print("Ocorreu um erro ao apagar a biblioteca", style="bold fg:darkred")
    else:
        questionary.print("Cancelado apagadamento da biblioteca", style="bold fg:darkgreen")
        
    questionary.press_any_key_to_continue("Pressione qualquer botão para continuar").ask()
    chamar_menu()


def editar_biblioteca():
    indice = int(questionary.text("Digite o nº da biblioteca que deseja editar:").ask()) - 1
    id_escolhido = obter_id_biblioteca(indice)

    response = requests.get(f"{url}/{id_escolhido}")
    biblioteca_escolhida = response.json()

    confirmacao: bool = bool(questionary.confirm("Tem certeza que deseja editar essa biblioteca:").ask())
    if confirmacao == True:
        dados_biblioteca = preencher_dados_biblioteca()
        response = requests.put(f"{url}/{biblioteca_escolhida['id']}", json=dados_biblioteca)   
        if response.status_code == 204:
            questionary.print("Biblioteca editada com sucesso", style="bold fg:darkgreen")
        else:
            questionary.print("Ocorreu um erro ao editar a biblioteca", style="bold fg:darkred")
    else:
        questionary.print("Cancelado edição da biblioteca", style="bold fg:darkgreen")
    
    questionary.press_any_key_to_continue("Pressione qualquer botão para continuar").ask()
    chamar_menu()
        

def obter_id_biblioteca(indice):
    response = requests.get(url)
    dados_json = response.json()
    # py estava entendo o indice 0 como None, então fiz o if para resolver o problema
    if indice == None:
        indice = 0
    
    id_escolhido: int = int((dados_json[indice])['id'])
    response = requests.get(f"{url}/{id_escolhido}")
    biblioteca_escolhida = response.json()
    
    console.print(
        f"[red]{biblioteca_escolhida['nome']}[/red]\n"
        f"[red]Endereço:[/red] {biblioteca_escolhida['endereco']}\n"
        f"[red]Cidade:[/red] {biblioteca_escolhida['cidade']} - {biblioteca_escolhida['estado']}\n"
        f"[red]CEP:[/red] [white]{biblioteca_escolhida['cep']}[/white]\n"
        f"[red]Telefone:[/red] [white]{biblioteca_escolhida['telefone']}[/white]\n"
        f"[red]E-mail:[/red] {biblioteca_escolhida['email']}\n"
        f"[red]Website:[/red] {biblioteca_escolhida['website']}\n"
        f"[red]Horário:[/red] [white]{biblioteca_escolhida['horarioAtendimento']}[/white]\n"
        f"[red]Data de criação:[/red] [white]{biblioteca_escolhida['dataCriacao']}[/white]",
    style="white b")

    return id_escolhido


def preencher_dados_biblioteca():
    nome = questionary.text("Digite o nome:").ask()
    estado = questionary.select("Escolha um estado:",choices=["SC", "PR"]).ask()
    if estado == "SC":
        cidade = questionary.select("Escolha uma cidade:", choices=["Indaial", "Blumenau", "Pomerode"]).ask()
    else:
        cidade = questionary.select("Escolha uma cidade:", choices=["Curitiba", "Colombo"]).ask()
    endereco = questionary.text("Digite o endereço:").ask()
    cep = questionary.text("Digite o CEP:").ask()
    telefone = questionary.text("Digite o telefone:").ask()
    email = str(f"{nome}.{estado}.biblioteca@gmail.com").lower().replace(" ", "")
    website = str(f"biblioteca.{nome}.{cidade}.com").lower().replace(" ", "")
    horario_atendimento = questionary.select("Escolha o horário de atendimento:", choices=["10h às 16h", "8h às 18h30", "12h às 17h."]).ask()
    data_criacao = str(datetime.datetime.now())
    
    dados_biblioteca = {
        'nome': nome, 'endereco': endereco, 'cidade': cidade, 'estado': estado, 'cep': cep, 'telefone': telefone, 'email': email, 'website': website, 'horarioAtendimento': horario_atendimento, 'dataCriacao': data_criacao 
    }

    return dados_biblioteca


def chamar_menu():
    time.sleep(1)
    console.rule("BibliOS", style="reverse")
    menu = questionary.select("Escolha uma opção:", choices=["Listar bibliotecas","Cadastrar biblioteca","Apagar biblioteca","Editar biblioteca", "Limpar terminal", "Sair"], style=custom_style_fancy).ask()
    if menu == "Listar bibliotecas":
        listar_bibliotecas()
    elif menu == "Cadastrar biblioteca":
        cadastrar_biblioteca()
    elif menu == "Apagar biblioteca":
        apagar_biblioteca()
    elif menu == "Editar biblioteca":
        editar_biblioteca()
    elif menu == "Limpar terminal":
        os.system('cls' if os.name == 'nt' else 'clear')
        chamar_menu()
    elif menu == "Sair":
        os.system('cls' if os.name == 'nt' else 'clear')
        questionary.print("BlibiOS Encerrado", style="bold fg:darkgreen")
        exit()
    else:
        questionary.print("Opção Inválida", style="bold fg:darkred")


chamar_menu()
