import questionary
from datetime import datetime

from database import session
from models import Livro, Autor


def cadastrar_livro():
    nome = input("Digite o nome: ")
    genero = input("Digite o gênero: ")
    data_lancamento = datetime.strptime(input("Digite a data de lançamento (dd/mm/yyyy): "), "%d/%m/%Y").date()
    id_autor = int(input("Digite o id do autor: "))

    livro = Livro(nome=nome, genero=genero, data_lancamento=data_lancamento, id_autor=id_autor)

    session.add(livro)
    session.commit()

    print("Livro cadastrado com sucesso!")


def listar_livros():
    livros = session.query(Livro).all()

    for livro in livros:
        print(
            f"ID: {livro.id} | "
            f"Nome: {livro.nome} | "
            f"Gênero: {livro.genero} | "
            f"Data de lançamento: {livro.data_lancamento} | "
            f"Disponível: {livro.disponibilidade} | "
            f"ID do autor: {livro.id_autor}"
        )


def alterar_livro():
    listar_livros()

    id_livro = int(input("Digite o ID do livro que deseja alterar: "))

    livro = session.query(Livro).filter_by(id=id_livro).first()

    livro.nome = input("Digite o novo nome: ")
    livro.genero = input("Digite o novo gênero: ")
    livro.data_lancamento = datetime.strptime(input("Digite a nova data de lançamento (dd/mm/yyyy): "), "%d/%m/%Y").date()
    livro.disponibilidade = bool(int(input("O livro está disponível? (1-Sim / 0-Não): ")))
    livro.id_autor = int(input("Digite o novo ID do autor: "))

    session.commit()

    print("Livro alterado com sucesso!")


def excluir_livro():
    listar_livros()

    id_livro = int(input("Digite o ID do livro que deseja deletar: "))

    livro = session.query(Livro).filter_by(id=id_livro).first()

    session.delete(livro)
    session.commit()

    print("Livro excluído com sucesso!")


def cadastrar_autor():
    nome = input("Digite o nome: ")
    data_nascimento = datetime.strptime(input("Digite a data de nascimento (dd/mm/yyyy): "), "%d/%m/%Y").date()
    nacionalidade = input("Digite a nacionalidade (XXX): ")

    autor = Autor(nome=nome, data_nascimento=data_nascimento, nacionalidade=nacionalidade)

    session.add(autor)
    session.commit()

    print("Autor cadastrado com sucesso!")


def listar_autores():
    autores = session.query(Autor).all()

    for autor in autores:
        print(
            f"ID: {autor.id} | "
            f"NOME: {autor.nome} | " 
            f"DATA DE NASCIMENTO: {autor.data_nascimento} | "
            f"NACIONALIDADE: {autor.nacionalidade}"
        )


def alterar_autor():
    listar_autores()

    id_autor = int(input("Digite o ID do autor que deseja alterar: "))

    livro = session.query(Autor).filter_by(id=id_autor).first()

    autor.nome = input("Digite o novo nome: ")
    autor.data_nascimento = datetime.strptime(input("Digite a nova data de nascimento (dd/mm/yyyy): "), "%d/%m/%Y").date()
    autor.nacionalidade = input("Digite a nova nacionalidade: ")

    session.commit()

    print("Autor cadastrado com sucesso!")


def excluir_autor():
    listar_autores()

    id_autor = int(input("Digite o ID do autor que deseja deletar: "))

    autor = session.query(Autor).filter_by(id=id_autor).first()

    session.delete(autor)
    session.commit()

    print("Autor excluído com sucesso!")


def menu_principal():
    while True:
        opcao = questionary.select("===== BIBLIOTECA =====", choices=["Livros", "Autores", "Sair"]).ask()
        match opcao:
            case "Livros": menu_livros()
            case "Autores": menu_autores()
            case "Sair": break


def menu_livros():
    while True:
        opcao = questionary.select("===== LIVROS =====", choices=["Cadastrar", "Listar", "Alterar", "Excluir", "Voltar"]).ask()
        match opcao:
            case "Cadastrar": cadastrar_livro()
            case "Listar": listar_livros()
            case "Alterar": alterar_livro()
            case "Excluir": excluir_livro()
            case "Voltar": break


def menu_autores():
    while True:
        opcao = questionary.select("===== AUTORES =====", choices=["Cadastrar", "Listar", "Alterar", "Excluir", "Voltar"]).ask()
        match opcao:
            case "Cadastrar": cadastrar_autor()
            case "Listar": listar_autores()
            case "Alterar": alterar_autor()
            case "Excluir": excluir_autor()
            case "Voltar": break


menu_principal()