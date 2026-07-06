# Sistema de Gestao Interna de Lanchonete

Projeto Flask desenvolvido seguindo o padrao arquitetural MVC, com Blueprints, SQLAlchemy, SQLite e heranca de templates Jinja2.

## O que foi implementado

- Camada **Model** com SQLAlchemy.
- Classe abstrata `BaseModel` com `id`, `data_criacao` e `data_atualizacao`.
- Tabela `tabela_cliente`, herdando de `BaseModel`.
- Tabela `tabela_fornecedor`, herdando de `BaseModel`.
- Camada **Controller** organizada com Blueprints.
- Rotas GET e POST para clientes e fornecedores.
- Camada **View** com Jinja2.
- Template base com `{% extends %}` e `{% block %}`.
- Banco local SQLite criado automaticamente.
- Dados iniciais de exemplo para facilitar a apresentacao.

## Estrutura do projeto

```text
lanchonete_mvc_flask/
├── lanchonete/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── home_controller.py
│   │   ├── cliente_controller.py
│   │   └── fornecedor_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── cliente.py
│   │   └── fornecedor.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── clientes.html
│   │   └── fornecedores.html
│   └── app.py
├── requirements.txt
└── README.md
```

## Como executar

Entre na pasta do projeto:

```bash
cd lanchonete_mvc_flask
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute a aplicacao:

```bash
cd lanchonete
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Rotas principais

- `/` - Pagina inicial
- `/clientes/` - Listagem e cadastro de clientes
- `/fornecedores/` - Listagem e cadastro de fornecedores

## Observacoes

O banco SQLite fica dentro da pasta `lanchonete/instance/` e e criado automaticamente na primeira execucao da aplicacao.
