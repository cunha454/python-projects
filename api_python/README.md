# Projetos de API

Scripts de terminal que consomem a API online `https://api.franciscosensaulas.com`:

- `api_biblioteca.py`: CRUD de bibliotecas.
- `api_biblioteca_autor.py`: CRUD de autores.
- `api_trabalho_servico.py`: CRUD de serviços.

## Como iniciar

No Linux, execute:

```bash
cd api_python
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
python 'api_nome.py'
```

No Windows, execute:

```powershell
cd api_python
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python 'api_nome.py'
```
