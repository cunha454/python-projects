# Pong (Pygame)

## Como iniciar

Este projeto deve ser executado com Python **3.13.7**. O `pyenv` (ou uma
ferramenta equivalente) é necessário para instalar essa versão e selecioná-la
somente na pasta `pygame`, sem alterar a versão global do sistema.

No Linux, siga as instruções do repositório oficial do [`pyenv`](https://github.com/pyenv/pyenv)
para sua distribuição, instalando também as ferramentas de compilação e
bibliotecas exigidas.

No Windows, siga as instruções do repositório oficial do
[`pyenv-win`](https://github.com/pyenv-win/pyenv-win) para instalar o gerenciador
e configurar o terminal.

### Após instalar o `pyenv`

No Linux, execute:

```bash
cd pygame
pyenv install 3.13.7
pyenv local 3.13.7
python --version
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
python pong.py
```

No Windows, execute:

```powershell
cd pygame
pyenv install 3.13.7
pyenv local 3.13.7
python --version
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python pong.py
```

`pyenv local 3.13.7` cria `pygame/.python-version` e aplica a versão somente
nessa pasta e em seus subdiretórios. Para voltar à versão global, remova esse
arquivo.

Pressione **Espaço** no menu para começar, mova a raquete esquerda com **W/S** e use **Esc** para voltar.

