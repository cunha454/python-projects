from sqlalchemy import Column, String, Integer, Boolean, Date, CHAR, ForeignKey
from sqlalchemy.orm import declarative_base

from database import db


Base = declarative_base()


class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100))
    genero = Column("genero", String(50))
    data_lancamento = Column("data_lancamento", Date)
    disponibilidade = Column("disponibilidade", Boolean, default=True)
    id_autor = Column("id_autor", ForeignKey("autores.id"))


class Autor(Base):
    __tablename__ = "autores"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100))
    data_nascimento = Column("data_nascimento", Date)
    nacionalidade = Column("nacionalidade", CHAR(3))


Base.metadata.create_all(db)