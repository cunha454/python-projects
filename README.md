# Test Python

Repositório destinado ao desenvolvimento de projetos em **Python**, com foco em estudos e prática de programação.

---

# Projetos

## API Python

Projeto desenvolvido para praticar o consumo de APIs utilizando Python e a biblioteca `requests`, implementando operações básicas de **CRUD** (Create, Read, Update e Delete).

### `api_biblioteca_autor.py`

Aplicação responsável pelo gerenciamento de autores.

Funcionalidades:
- Cadastrar autores;
- Listar autores;
- Editar informações;
- Remover autores.

Dados trabalhados:
- Nome;
- Nacionalidade;
- Data de nascimento.

---

### `api_trabalho_servico.py`

Aplicação para gerenciamento de serviços.

Funcionalidades:
- Cadastrar serviços;
- Listar serviços;
- Editar informações;
- Remover serviços.

Dados trabalhados:
- Nome;
- Preço;
- Duração.

Recursos utilizados:
- `requests` para comunicação com a API;
- `rich` para melhorar a visualização e organização da interface no terminal.

---

### `api_biblioteca.py`

Aplicação para gerenciamento de bibliotecas utilizando uma API.

Funcionalidades:
- Cadastrar bibliotecas;
- Listar bibliotecas;
- Editar informações;
- Remover bibliotecas.

Dados trabalhados:
- Nome;
- Endereço;
- Cidade;
- Estado;
- CEP;
- Telefone;
- E-mail;
- Website;
- Horário de atendimento;
- Data de criação.

Recursos utilizados:
- `requests` para comunicação com a API;
- `rich` para estilização do terminal;
- `questionary` para criação de menus interativos.

---

# Pygame

Projetos desenvolvidos utilizando a biblioteca `pygame`, explorando conceitos de programação de jogos 2D, movimentação, colisões, eventos e renderização gráfica.

## `pong.py`

Implementação do clássico jogo **Pong**.

Funcionalidades:
- Controle do jogador;
- Movimentação automática do adversário;
- Sistema de colisão entre objetos;
- Sistema de pontuação;
- Renderização de textos na tela;
- Centralização de elementos;
- Reprodução de efeitos sonoros.

Recursos utilizados:
- Biblioteca `pygame` para criação do jogo e gerenciamento dos elementos gráficos.