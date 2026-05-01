# 💰 FinTrack API

> **API RESTful para gerenciamento financeiro pessoal**, desenvolvida com Python e FastAPI, com banco de dados MongoDB.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)]()
[![License](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)](LICENSE)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Rodar Localmente](#-como-rodar-localmente)
- [Endpoints](#-endpoints)
- [Roadmap](#-roadmap)
- [Autor](#-autor)

---

## 📖 Sobre o Projeto

A **FinTrack API** é o backend de um sistema de controle financeiro pessoal. O objetivo é oferecer uma API robusta e escalável para registrar receitas, despesas, categorias e gerar relatórios financeiros — servindo como base para aplicações web ou mobile de finanças.

O projeto foi criado com foco em **boas práticas de desenvolvimento backend**, uso de frameworks modernos e fortalecimento de portfólio profissional.

---

## ✅ Funcionalidades

- [x] Estrutura base da API com FastAPI
- [x] Conexão com banco de dados MongoDB via PyMongo
- [x] Documentação automática via Swagger UI (`/docs`)

---

## 🛠️ Tecnologias

| Tecnologia | Descrição |
|---|---|
| **Python 3.10+** | Linguagem principal |
| **FastAPI** | Framework web moderno e de alta performance |
| **Uvicorn** | Servidor ASGI para rodar a aplicação |
| **Pydantic** | Validação de dados e schemas |
| **PyMongo** | Driver oficial do MongoDB para Python |
| **MongoDB** | Banco de dados NoSQL orientado a documentos |

---

## 📁 Estrutura do Projeto

```
FinTrack-API/
├── app/
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── routes/          # Definição das rotas/endpoints
│   ├── models/          # Modelos Pydantic (schemas)
│   ├── database/        # Configuração de conexão com MongoDB
│   └── services/        # Regras de negócio
├── requitements.txt     # Dependências do projeto
└── README.md
```

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.10+
- MongoDB rodando localmente

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/guinixon/FinTrack-API.git
cd FinTrack-API
```

**2. Crie e ative um ambiente virtual**
```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requitements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=fintrack
```

**5. Inicie o servidor**
```bash
uvicorn app.main:app --reload
```

**6. Acesse a documentação interativa**

Abra o navegador em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 Endpoints

> A documentação completa e interativa está disponível via **Swagger UI** em `/docs` ao rodar a aplicação.

| Método | Rota | Descrição | Status |
|---|---|---|---|
| `GET` | `/transactions` | Listar todas as transações | ✅ Implementado |
| `POST` | `/transactions` | Criar nova transação | ✅ Implementado |
| `PUT` | `/transactions/{id}` | Atualizar transação | 🔜 Planejado |
| `DELETE` | `/transactions/{id}` | Remover transação | 🔜 Planejado |
| `GET` | `/categories` | Listar categorias | 🔜 Planejado |
| `GET` | `/reports/monthly` | Relatório mensal | 🔜 Planejado |

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme** — projeto de portfólio para estudo e prática de desenvolvimento backend com Python.

[![GitHub](https://img.shields.io/badge/GitHub-guinixon-181717?style=flat-square&logo=github)](https://github.com/guinixon)
