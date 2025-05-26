🎓 API de Gerenciamento Escolar
Este repositório contém a API de Gerenciamento Escolar, desenvolvida com Flask e SQLAlchemy. A API faz parte de uma arquitetura modular baseada em microsserviços e é responsável pelo gerenciamento de alunos, professores e turmas em uma instituição de ensino.

🧩 Arquitetura
A API foi construída com uma estrutura clara e organizada, utilizando o padrão de camadas, separando controllers, models e rotas (namespaces). Além disso, ela conta com documentação interativa via Swagger e está preparada para deploy em nuvem com Docker, Render e arquivos auxiliares como Procfile e render.yaml.

🚀 Tecnologias Utilizadas
Python 3.x

Flask

Flask-RESTx (Swagger + Namespaces)

SQLAlchemy

SQLite (banco de dados local)

Docker

Render (para deploy)

Docker Compose

Git

▶️ Como Executar a API Localmente
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/hermosoarthur/API-FLASK
cd gerenciamento-escolar
Executar com Docker (recomendado):

bash
Copiar
Editar
docker-compose up --build
Ou executar manualmente:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python app.py
A aplicação estará disponível em: 📍 http://localhost:5000
A documentação Swagger pode ser acessada em: 📍 http://localhost:5000/docs

📡 Endpoints Principais
📘 Alunos
GET /alunos

GET /alunos/<id>

POST /alunos

PUT /alunos/<id>

DELETE /alunos/<id>

👨‍🏫 Professores
GET /professores

GET /professores/<id>

POST /professores

PUT /professores/<id>

DELETE /professores/<id>

🏫 Turmas
GET /turmas

GET /turmas/<id>

POST /turmas

PUT /turmas/<id>

DELETE /turmas/<id>

📦 Estrutura do Projeto
bash
Copiar
Editar
gerenciamento-escolar/
│
├── app.py                  # Arquivo principal da aplicação
├── config.py               # Configurações gerais da aplicação
├── requirements.txt        # Dependências do projeto
├── Dockerfile              # Configuração para container Docker
├── docker-compose.yml      # Orquestração com Docker Compose
├── Procfile                # Arquivo para deploy no Render
├── render.yaml             # Configuração de deploy Render
├── README.md               # Documentação do projeto
├── teste.py                # Script de testes simples
│
├── controllers/            # Controladores da lógica de negócio
│   └── aluno_controller.py
│   └── professor_controller.py
│   └── turma_controller.py
│
├── models/                 # Definições de modelos SQLAlchemy
│   └── aluno_model.py
│   └── professor_model.py
│   └── turma_model.py
│
└── swagger/                # Documentação Swagger (Flask-RESTx)
    └── namespaces.py
🛠️ Futuras Melhorias
Autenticação JWT para usuários

Relacionamento entre alunos, professores e turmas

Validações avançadas com Marshmallow

Paginação e filtros nos endpoints

Integração com API externa (ex: reservas, biblioteca)

Geração de relatórios (boletins, frequência, etc.)



🧑‍💻 Autores
Nomes dos desenvolvedores – 
Arthur Hermoso                  2401651
Luana Garrido Moreira Dias 	    2501736
Rafala Santos Rodrigues        	2402206
Vitória da Silva Moço        	2401868
Fanthine Vitoria de Souza	    2401012