# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: _______________________________
- Turma: _______________________________

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.

Caminho: Aula12_24_06/models/

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?

O arquivo criado é o streamflix.db
Esta configuração de inicialização e conexão com o banco de dados está localizada no arquivo app.py na raiz do projeto.


**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?

FilmeFavorito localizada no arquivo models/filme_favorito.py
HistoricoBusca localizada no arquivo models/historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?

Superclasse: Ambas herdam da superclasse ModeloBase.
Campos herdados automaticamente: 
1. id
2. data_criacao
3. data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?

__tablename__: O nome da tabela é "filmes_favoritos".

Motivo de usar: Usamos o __tablename__ para forçar um padrão explícito e amigável de nomenclatura no banco de dados (geralmente letras minúsculas e no plural com sublinhados), em vez de deixar o SQLAlchemy gerar um nome padrão baseado no padrão PascalCase da classe (FilmeFavorito).

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?

Coluna: A coluna é a tmdb_id.
Restrições especiais: Sim, ela possui nullable=False (obrigatória/não aceita valores nulos) e unique=True (o valor deve ser único, impedindo duplicatas do mesmo filme).

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

Primeiro, ele chama cls.buscar_por_tmdb(tmdb_id) para verificar se o filme já foi salvo.
Se não existir, ele cria uma nova instância de FilmeFavorito com os parâmetros fornecidos (tmdb_id, titulo, poster_path, nota, ano).
Adiciona o objeto à sessão do banco de dados com db.session.add(fav).
Salva permanentemente no banco com db.session.commit().
Retorna o objeto criado (fav).
Se o filme já existir: O método interrompe a execução imediatamente e retorna None, sem adicionar nada ao banco.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

Onde está (arquivo): No arquivo models/historico_busca.py.
Nome da classe: HistoricoBusca
Nome do método: ultimas(cls, limite=8)

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

4 campos salvos:
tmdb_id
titulo
poster_path
nota

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

O que é exportado além de db: São exportados a classe ModeloBase, a classe FilmeFavorito e a classe HistoricoBusca (definidos explicitamente na lista __all__).
Por que o controller importa dessa forma: Porque o arquivo __init__.py transforma a pasta models em um pacote unificado. Isso permite importar as classes diretamente do pacote central de modelos de forma mais limpa, em vez de exigir caminhos longos e acoplados como from models.filme_favorito import FilmeFavorito.
---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).

Dashboard / Home Blueprint (no arquivo dashboard_controller.py) – geralmente mapeado para a raiz ou /dashboard.
Favoritos Blueprint (no arquivo favoritos_controller.py) – geralmente com o prefixo url_prefix='/favoritos'.
Filmes Blueprint (no arquivo filmes_controller.py) – geralmente com o prefixo url_prefix='/filmes'.

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?

A função que responde essa rota é:
populares()

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).

Cria um objeto da classe TmdbApi e chama:
api.filmes_populares()
Chama o Model:
FilmeFavorito.listar()

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?

O termo é registrado no arquivo:
controllers/filmes_controller.py
O Model utilizado é:
HistoricoBusca.registrar(termo, len(filmes))

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?

O método HTTP exigido é:
POST

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?

Se o filme não for encontrado (None), o usuário é redirecionado para a página de filmes populares através de:
redirect(url_for("filmes.populares"))

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).

Os Blueprints são registrados no arquivo:
app.py
app.register_blueprint(dashboard_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?

O controller é:
controllers/dashboard_controller.py
A função é:
index()

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?

Camada: Ela pertence à camada de Service (Serviço).
Justificativa: Ela é uma classe de integração externa. Ela é chamada exclusivamente pelos Controllers (como filmes_controller.py) para consumir os dados de filmes diretamente da API pública do TMDB, antes que esses dados sejam enviados para renderização na View ou salvos no banco através do Model.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.

Quando a requisição é GET, utiliza:
request.args
Quando a requisição é POST, utiliza:
request.form

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?

Os templates ficam em:
views/templates/

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?

O template base é:
views/templates/layout.html
Os outros templates utilizam:
{% extends "layout.html" %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.

url_for('dashboard.index')
(StreamFlix)

url_for('filmes.populares')
(Populares)

url_for('filmes.melhores')
(Melhores)

url_for('filmes.buscar')
(Buscar)

url_for('favoritos.listar')
(Favoritos)

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?

Arquivo:
views/templates/filmes/detalhe.html
A variável streaming vem do controller:
streaming, demo = api.streaming(filme_id)
da classe TmdbApi, em controllers/filmes_controller.py.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?

É um pedaço reutilizado (template parcial).
Ele é incluído pelos templates de listagem utilizando a tag Jinja:
{% include "filmes/_card.html" %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?

A View verifica a variável:
favorito
Se existir:
{% if favorito %}

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?

O CSS está em:
views/static/css/style.css
É carregado com:
url_for('static', filename='css/style.css')

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.

Loop:
{% for fav in favoritos %}
Três campos exibidos:
titulo
nota
ano
(Também aparece a data de criação.)

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?

Ela verifica se o sistema está funcionando em modo demonstração.
A variável é disponibilizada para todos os templates pelo context processor definido no arquivo app.py:
@app.context_processor

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite 
arquivos envolvidos.

O usuário clica no botão Salvar favorito em:
views/templates/filmes/detalhe.html

O formulário envia uma requisição POST para:
/favoritos/adicionar/<tmdb_id>

A requisição é recebida pelo controller:
controllers/favoritos_controller.py

na função:

adicionar()
O controller chama o Model:

FilmeFavorito.adicionar(...)
O Model grava o filme no banco SQLite.

Após salvar, o controller executa:
redirect(voltar)

O navegador retorna para a página de detalhes do filme, onde agora aparece o botão Remover dos favoritos.

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
