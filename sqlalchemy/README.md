# Biblioteca com SQLAlchemy

Aplicação de terminal para CRUD de livros e autores em MySQL.

## Como iniciar

No Linux, execute:

```bash
cd sqlalchemy
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

No Windows, execute:

```powershell
cd sqlalchemy
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Crie o arquivo `sqlalchemy/.env`:

```dotenv
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_NAME=biblioteca
```

Depois execute:

```bash
cd sqlalchemy/biblioteca
python main.py
```

O banco e as tabelas são criados automaticamente na primeira execução.

Opcionalmente, depois que o banco e as tabelas forem criados, insira dados de
exemplo diretamente no MySQL executando o arquivo `banco_de_dados.sql`:

```bash
mysql -u seu_usuario -p biblioteca < sqlalchemy/biblioteca/banco_de_dados.sql
```

O arquivo insere 10 autores e 20 livros.
