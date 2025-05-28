# 🎓 API de Gerenciamento Escolar
Este repositório contém a API de Gerenciamento Escolar, desenvolvida com Flask e SQLAlchemy.
A API faz parte de uma arquitetura modular baseada em microsserviços e é responsável pelo gerenciamento de alunos, professores e turmas em uma instituição de ensino.

## 🧩 Arquitetura
A API foi construída com uma estrutura clara e organizada, utilizando o padrão de camadas, separando controllers, models e rotas (namespaces).
Conta também com documentação interativa via Swagger e está preparada para deploy em nuvem com Docker, Render e arquivos auxiliares como Procfile e render.yaml.

## 🚀 Tecnologias Utilizadas
Python 3

Flask

Flask-RESTx (Swagger + Namespaces)

SQLAlchemy

SQLite (banco de dados local)

Docker

Render (para deploy)

Git

## ▶️ Como Executar a API com Docker

1. **Clone o repositório:**
```bash
git clone https://github.com/hermosoarthur/API-FLASK
cd API-FLASK
```                                                                                                                                                                                                     
2. Executar com Docker (recomendado):
```bash
docker network create api-network
```
Essa rede será utilizada por todas as APIs que fazem parte do sistema de microsserviços (como as APIs de Atividades e Reservas), permitindo que elas se comuniquem entre si.

3. Construa a imagem da API
```bash
docker build -t api-flask .
```
4. Execute o container utilizando a rede criada:
```bash
docker run -d --name api-flask --network api-network -p 5000:5000 api-flask
```

## 🔗 Acesse:
Aplicação: http://localhost:5000/projeto-api-flask/

Documentação Swagger: http://localhost:5000/docs

## 📡 Endpoints Principais
## 📘 Alunos
GET /alunos

GET /alunos/<id>

POST /alunos

PUT /alunos/<id>

DELETE /alunos/<id>

## 👨‍🏫 Professores
GET /professores

GET /professores/<id>

POST /professores

PUT /professores/<id>

DELETE /professores/<id>

## 🏫 Turmas
GET /turmas

GET /turmas/<id>

POST /turmas

PUT /turmas/<id>

DELETE /turmas/<id>

## 📦 Estrutura do Projeto

```bash
API-FLASK/
│
├── app.py                  
├── config.py               
├── requirements.txt       
├── Dockerfile             
├── Procfile                
├── render.yaml             
├── README.md               
├── teste.py                
│
├── controllers/            
│   ├── aluno_controller.py
│   ├── professor_controller.py
│   └── turma_controller.py
│
├── models/                 
│   ├── aluno_model.py
│   ├── professor_model.py
│   └── turma_model.py
│
└── swagger/                
    └── namespaces.py
```

## 🛠️ Futuras Melhorias
Autenticação JWT para usuários

Relacionamento entre alunos, professores e turmas

Validações avançadas com Marshmallow

Paginação e filtros nos endpoints

Uso do docker compose

Geração de relatórios (boletins, frequência, etc.)



# 🧑‍💻 Autores

Nomes dos desenvolvedores:  
Arthur Hermoso ......................... 2401651  
Luana Garrido Moreira Dias ............ 2501736  
Rafaela Santos Rodrigues .............. 2402206  
Vitória da Silva Moço .................. 2401868  
Fanthine Vitoria de Souza ............. 2401012

