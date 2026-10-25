# 🛒 E-commerce UniFacisa

Aplicação web de e-commerce desenvolvida em Python com Flask, organizada em módulos para autenticação, gerenciamento de usuários, produtos e vendas.

O projeto utiliza uma arquitetura modular baseada em Blueprints, persistência de dados com Flask-SQLAlchemy e gerenciamento de sessões de autenticação com Flask-Login.

## ✨ Funcionalidades

- **Autenticação:** gerenciamento de login e controle de acesso às páginas protegidas.
- **Usuários:** módulo dedicado ao gerenciamento de usuários.
- **Produtos:** módulo para organizar as funcionalidades relacionadas aos produtos.
- **Vendas:** módulo dedicado às operações de vendas.
- **Templates HTML:** renderização das páginas no servidor.
- **Persistência de dados:** integração com banco de dados por meio do SQLAlchemy.
- **Configuração por ambiente:** utilização de variáveis de ambiente para configurar a conexão com o banco de dados e a chave secreta da aplicação.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| [Python](https://www.python.org/) | Linguagem de programação |
| [Flask](https://flask.palletsprojects.com/) | Framework web |
| [Flask-Login](https://flask-login.readthedocs.io/) | Gerenciamento de autenticação e sessões |
| [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) | Integração entre Flask e SQLAlchemy |
| [SQLAlchemy](https://www.sqlalchemy.org/) | Mapeamento objeto-relacional (ORM) |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Carregamento de variáveis de ambiente |
| HTML/CSS | Estrutura e apresentação das páginas |

## 📁 Estrutura do projeto

```text
ecommerce-unifacisa/
├── generic/
│   └── ...                 # Componentes genéricos e acesso a dados
├── login/
│   └── ...                 # Autenticação
├── products/
│   └── ...                 # Funcionalidades de produtos
├── sales/
│   └── ...                 # Funcionalidades de vendas
├── static/
│   └── ...                 # Arquivos estáticos
├── templates/
│   └── ...                 # Templates HTML
├── users/
│   └── ...                 # Funcionalidades de usuários
├── .env.example            # Exemplo de configuração do ambiente
├── .gitignore
├── app.py                  # Inicialização e configuração da aplicação
└── requirements.txt        # Dependências Python
```

### Organização da aplicação

A aplicação utiliza o sistema de Blueprints do Flask para separar diferentes áreas funcionais em módulos independentes.

O arquivo `app.py` centraliza a configuração da aplicação, inicializa a integração com o banco de dados, registra os Blueprints e configura o Flask-Login.

Essa organização facilita a manutenção, a separação de responsabilidades e a evolução do sistema.

## 🚀 Como executar

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.10 ou superior.
- Git.
- Um banco de dados compatível com a configuração do SQLAlchemy utilizada no projeto.

> **Observação:** a versão mínima de Python indicada é uma sugestão. O projeto não especifica uma versão mínima oficial.

### 1. Clone o repositório

```bash
git clone https://github.com/SymonBezerra/ecommerce-unifacisa.git
```

Entre no diretório do projeto:

```bash
cd ecommerce-unifacisa
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema operacional.

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando `.env.example` como referência.

```bash
cp .env.example .env
```

No Windows, você também pode copiar o arquivo manualmente.

Configure as seguintes variáveis:

```dotenv
DATABASE_URI=
SECRET_KEY=
```

- `DATABASE_URI`: string de conexão com o banco de dados.
- `SECRET_KEY`: chave secreta utilizada pelo Flask para proteger os dados de sessão.

**Importante:** utilize uma chave secreta forte e mantenha o arquivo `.env` fora do controle de versão. Não utilize uma chave padrão em ambientes de produção.

### 5. Execute a aplicação

O projeto define a aplicação Flask no objeto `app`, localizado em `app.py`.

Para iniciar o servidor de desenvolvimento, execute:

```bash
flask --app app run --debug
```

A aplicação estará disponível, por padrão, em:

http://127.0.0.1:5000

> A inicialização depende de uma configuração válida do banco de dados. O comando acima inicia o servidor de desenvolvimento do Flask, destinado a testes locais.

## ⚙️ Configuração do banco de dados

A conexão com o banco de dados é definida pela variável `DATABASE_URI`.

Exemplo de configuração para SQLite:

```dotenv
DATABASE_URI=sqlite:///ecommerce.db
SECRET_KEY=substitua-por-uma-chave-segura
```

Esse exemplo utiliza SQLite, desde que o ambiente e os modelos da aplicação sejam compatíveis com esse banco.

Para outros bancos de dados, configure a URI apropriada e instale o driver correspondente.

A aplicação utiliza Flask-SQLAlchemy para inicializar a integração com o banco de dados e executar `db.create_all()` durante a inicialização do contexto da aplicação.

Esse mecanismo cria as tabelas ausentes a partir dos modelos registrados, mas não substitui um sistema de migrações para gerenciar alterações de esquema ao longo do tempo.

## 🔐 Autenticação

O projeto utiliza Flask-Login para gerenciar a autenticação dos usuários.

O mecanismo de autenticação é inicializado em `app.py`, que também define o carregamento do usuário a partir de seu identificador.

A rota principal (`/`) exige autenticação. Usuários não autenticados são direcionados para a rota de login configurada pela aplicação.

## 🧪 Testes

A estrutura atual do repositório não apresenta uma suíte de testes automatizados identificável.

Para evoluir o projeto, recomenda-se adicionar testes para:

- Autenticação e encerramento de sessão.
- Acesso às rotas protegidas.
- Operações de gerenciamento de produtos.
- Operações de vendas.
- Persistência e integridade dos dados.
- Validação de entradas e tratamento de erros.

O [pytest](https://docs.pytest.org/) pode ser utilizado para implementar esses testes.

## 🔒 Boas práticas de segurança

- Nunca versione credenciais ou chaves secretas.
- Utilize variáveis de ambiente para configurações sensíveis.
- Não utilize o servidor de desenvolvimento do Flask em produção.
- Valide os dados recebidos pelos formulários.
- Verifique as permissões de acesso às operações de gerenciamento.
- Considere implementar migrações de banco de dados para controlar alterações nos modelos.
- Utilize HTTPS e configurações de sessão apropriadas ao ambiente de produção.

## 🗺️ Possíveis melhorias

Algumas evoluções que podem contribuir para a maturidade do projeto:

- Implementar testes automatizados com pytest.
- Adotar migrações de banco de dados com Flask-Migrate e Alembic.
- Melhorar o tratamento de erros e a validação de formulários.
- Implementar controle de permissões por perfil de usuário.
- Documentar os fluxos de gerenciamento de produtos e vendas.
- Adicionar instruções de implantação em ambiente de produção.
- Automatizar verificações de qualidade com integração contínua.

## 👨‍💻 Autor

**Symon Bezerra**

- GitHub: [@SymonBezerra](https://github.com/SymonBezerra)
- Repositório: [ecommerce-unifacisa](https://github.com/SymonBezerra/ecommerce-unifacisa)

---

Desenvolvido como projeto de aplicação web utilizando Python e Flask.