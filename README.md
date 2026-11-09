# POC - API com Django Rest Framework

Prova de conceito (POC) de uso de API com Django Rest Framework, MongoDB e documentação automática via Swagger (drf-yasg).

## Tecnologias

- [Django](https://www.djangoproject.com/) 4.2 LTS
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MongoDB](https://www.mongodb.com/) (via [djongo](https://github.com/nesdis/djongo))
- [drf-yasg](https://drf-yasg.readthedocs.io/) — Swagger UI
- [uv](https://github.com/astral-sh/uv) — gerenciador de pacotes e ambientes Python
- [Docker](https://www.docker.com/) + Docker Compose
- [pytest](https://docs.pytest.org/) + [pytest-django](https://pytest-django.readthedocs.io/) — testes
- [coverage](https://coverage.readthedocs.io/) — relatório de cobertura de testes

## Estrutura do projeto

```text
cinema-api/
├── config/              # Pacote de configuração do Django (settings, urls, wsgi, asgi)
├── movies/              # App: filmes (CRUD)
├── theaters/            # App: teatros/salas (CRUD)
├── sessions/            # App: sessões de cinema (CRUD, com FK para filme e teatro)
├── .github/workflows/   # CI (GitHub Actions)
├── Dockerfile           # Imagem da API
├── docker-compose.yml   # Orquestração: API + MongoDB
├── pyproject.toml       # Dependências e config do uv
├── .env.example         # Exemplo de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo git
├── manage.py            # Utilitário do Django
└── README.md
```

## Endpoints da API

| Recurso | Método | Endpoint | Descrição |
|---------|--------|----------|-----------|
| Filmes | GET | `/api/movies/` | Listar todos os filmes |
| Filmes | POST | `/api/movies/` | Criar um filme |
| Filmes | GET | `/api/movies/<name>/` | Detalhar um filme |
| Filmes | PUT | `/api/movies/<name>/` | Atualizar um filme |
| Filmes | DELETE | `/api/movies/<name>/` | Remover um filme |
| Teatros | GET | `/api/theaters/` | Listar todos os teatros |
| Teatros | POST | `/api/theaters/` | Criar um teatro |
| Teatros | GET | `/api/theaters/<number>/` | Detalhar um teatro |
| Teatros | PUT | `/api/theaters/<number>/` | Atualizar um teatro |
| Teatros | DELETE | `/api/theaters/<number>/` | Remover um teatro |
| Sessões | GET | `/api/sessions/` | Listar todas as sessões |
| Sessões | POST | `/api/sessions/` | Criar uma sessão |
| Sessões | GET | `/api/sessions/<id>/` | Detalhar uma sessão |
| Sessões | PUT | `/api/sessions/<id>/` | Atualizar uma sessão |
| Sessões | DELETE | `/api/sessions/<id>/` | Remover uma sessão |
| Admin | — | `/admin/` | Painel administrativo do Django |
| Swagger | — | `/` | Documentação interativa da API |

## Como executar o projeto

### Opção 1: Docker (recomendado)

Inicializa a API e o MongoDB em containers:

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd cinema-api

# Copie o arquivo de variáveis de ambiente
cp .env.example .env

# Suba os containers
docker compose up --build
```

Acesse:
- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/`
- MongoDB: `localhost:27017`

Para encerrar:
```bash
docker compose down
```

### Opção 2: uv sync

O [uv](https://github.com/astral-sh/uv) cria o ambiente virtual e instala as dependências automaticamente:

```bash
# Instale o uv (se ainda não tiver)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sincronize dependências (incluindo dev)
uv sync --dev

# Copie as variáveis de ambiente
cp .env.example .env

# Rode as migrações (MongoDB não exige migrações tradicionais, mas o comando prepara o projeto)
uv run python manage.py migrate 2>/dev/null || true

# Inicie o servidor
uv run python manage.py runserver
```

Acesse:
- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/`

### Opção 3: venv + pip (alternativa)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# ou: .venv\Scripts\activate  # Windows

pip install -r pyproject.toml  # ou instale manualmente:
pip install Django djangorestframework drf-yasg djongo python-dotenv pytest pytest-django coverage

cp .env.example .env
python manage.py runserver
```

## Variáveis de ambiente

Crie um arquivo `.env` a partir do `.env.example`:

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DJANGO_SECRET_KEY` | `django-insecure-dev-key-change-in-production` | Chave secreta do Django |
| `DJANGO_DEBUG` | `True` | Modo debug |
| `DJANGO_ALLOWED_HOSTS` | `*` | Hosts permitidos |
| `MONGO_URI` | `mongodb://localhost:27017` | URI de conexão com MongoDB |
| `MONGO_DB_NAME` | `cinema_db` | Nome do banco de dados |

## Testes da API

Os testes cobrem CRUD completo de filmes, teatros e sessões:

```bash
# Com uv
uv sync --dev
uv run coverage run -m pytest
uv run coverage report

# Ou apenas pytest
uv run pytest
```

### Resultados gráficos dos testes

O projeto gera relatório de cobertura em HTML. Após executar os testes com coverage:

```bash
uv run coverage html
```

Abra `htmlcov/index.html` no navegador para visualizar os resultados gráficos da cobertura de código.

No GitHub Actions, cada push/pull request executa os testes e publica o relatório de cobertura como artefato.

## Documentação Swagger

A documentação interativa está disponível automaticamente na raiz da API:

```
http://localhost:8000/
```

Permite testar todos os endpoints (GET, POST, PUT, DELETE) diretamente pelo navegador.

## Banco de dados

Este projeto utiliza **MongoDB** em vez de SQLite. O conector `djongo` permite continuar usando o Django ORM com o Django REST Framework, sem alterar a forma como modelos, serializers e views são escritos.

Não há arquivo `db.sqlite3` no repositório.

## Licença

MIT
