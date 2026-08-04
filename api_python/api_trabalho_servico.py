import time
import requests
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich import box
from rich.theme import Theme

url = "https://api.franciscosensaulas.com/api/v1/trabalho/servicos"
tema = Theme({
    "sucesso": "bold green",
    "erro": "bold red"
})
console = Console(theme=tema)

def listar_servicos():
    response = requests.get(url)
    dados_json = response.json()
    i = 1

    tabela = Table(title="Sistema Serviços", show_lines=True, box=box.MARKDOWN, title_style="reverse #415A77")
    tabela.add_column("N°", justify="left", style="#243010")
    tabela.add_column("Serviço", justify="left", style="#EECF6D")
    tabela.add_column("Preço", justify="left", style="#011638")
    tabela.add_column("Duração", justify="left", style="#720E07" )

    for servico in dados_json:
        tabela.add_row(f"{i}", f"{servico['nome']}", f"R$ {servico['preco']}", f"{servico['duracao']} minutos")
        i = i + 1

    console = Console()
    console.print(tabela)


def cadastrar_servico():
    servico_nome: str = Prompt.ask("Digite o serviço desejado", choices=["Manutenção Preventiva", "Troca de Pasta Térmica", "Reparos de Hardware", "Formatação e Instalção de SO", "Cable Management"], default="Manutenção Preventiva", case_sensitive=False)
    servico_preco: float = float(Prompt.ask("Digite o valor do serviço"))
    servico_duracao: int = int(Prompt.ask("Digite a duração do serviço"))

    dados_servico = {
        'nome': servico_nome, 'preco': servico_preco, 'duracao': servico_duracao
    }

    response = requests.post(url, json=dados_servico)
    if response.status_code == 201:
        console.print("O serviço foi cadastrado com sucesso", style="sucesso")
        time.sleep(1)
        console.clear(home=True)
    else:
        console.print("Ocorreu um erro ao cadastrar o serviço")


def apagar_servico():
    indice_escolhido: int = int(Prompt.ask("Digite o índice do serviço que deseja apagar"))
    servico_escolhido = obter_id_servico(indice_escolhido)

    response = requests.get(f"{url}/{servico_escolhido}")
    item = response.json()
    console.print(f"Serviço Selecionado: {item['nome']} | R${item['preco']} | {item['duracao']} minutos", style="red")
    confimacao: str = Prompt.ask("TEM CERTEZA QUE QUER EXCLUIR ESSE SERVIÇO (y/n)").lower()
    if confimacao == "y":
        response = requests.delete(f"{url}/{servico_escolhido}")
        if response.status_code == 204:
            console.print("Serviço apagado com sucesso", style="sucesso")
            time.sleep(1)
            console.clear(home=True)
        else:
            console.print("Ocorreu um erro ao apagar o serviço", style="erro")
    elif confimacao == "n":
        console.print("O processo de apagamento foi cancelado", style="sucesso")
    else:
        console.print("Opção inválida", style="erro")

    return indice_escolhido


def editar_servico():
    indice_escolhido: int = int(Prompt.ask("Digite o índice do serviço que deseja editar"))
    servico_escolhido = obter_id_servico(indice_escolhido)

    response = requests.get(f"{url}/{servico_escolhido}")
    item = response.json()
    console.print(f"Serviço Selecionado: {item['nome']} | R${item['preco']} | {item['duracao']} minutos", style="red")

    novo_valor_servico: str = Prompt.ask("Digite o serviço desejado", choices=["Manutenção Preventiva", "Troca de Pasta Térmica", "Reparos de Hardware", "Formatação e Instalção de SO", "Cable Management"], default="Manutenção Preventiva", case_sensitive=False)
    novo_valor_preco: float = float(Prompt.ask("Digite o valor do serviço"))
    novo_valor_duraco: int = int(Prompt.ask("Digite a duração do serviço"))

    novo_dados_servico = {
       'nome': novo_valor_servico, 'preco': novo_valor_preco, 'duracao': novo_valor_duraco
    }
    response = requests.put(f"{url}/{servico_escolhido}", json=novo_dados_servico)
    if response.status_code == 204:
        console.print("Serviço editado com sucesso", style="sucesso")
        time.sleep(1)
        console.clear(home=True)
    else:
        console.print("Ocorre um erro ao editar o serviço", style="erro")

    return indice_escolhido


def obter_id_servico(indice_escolhido):
    response = requests.get(url)
    dados_json = response.json()

    servico_escolhido = dados_json[indice_escolhido - 1]['id']
    
    return servico_escolhido


escolha = -1
while escolha != 0:
    time.sleep(0.5)
    console.print("API TRABALHO SERVIÇOS", style="reverse")
    console.print("1 - Listar serviços\n2 - Cadastrar serviço\n3 - Apagar serviço\n4 - Editar serviço\n0 - Sair", style="b")
    escolha: int = int(Prompt.ask("Digite sua escolha"))
    if escolha == 1:
        listar_servicos()
    elif escolha == 2:
        cadastrar_servico()
    elif escolha == 3:
        obter_id_servico(apagar_servico())
    elif escolha == 4:
        obter_id_servico(editar_servico())
    elif escolha == 0:
        console.print("Sistema encerrado", style="sucesso")
        time.sleep(1)
        console.clear(home=True)
    else:
        console.print("Opção inválida", style="erro")
        time.sleep(1)
        console.clear(home=True)


