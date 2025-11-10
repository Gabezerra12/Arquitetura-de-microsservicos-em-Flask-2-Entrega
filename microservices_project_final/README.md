# Projeto Final - Microsserviços (Gerenciamento, Reservas, Atividades)

Este repositório contém três microsserviços em Flask, cada um com arquitetura MVC, banco SQLite independente via SQLAlchemy, documentação Swagger (Flasgger), e comunicação síncrona via `requests`. Os bancos são entregues vazios (sem dados de seed).

## Serviços e portas
- Gerenciamento: http://localhost:5000 (Swagger: /apidocs)
- Reservas: http://localhost:5001 (Swagger: /apidocs)
- Atividades: http://localhost:5002 (Swagger: /apidocs)

## Como executar
Pré-requisitos: Docker e Docker Compose instalados.
No diretório raiz execute:
```
docker compose up --build
```
Para parar e remover containers:
```
docker compose down
```

## Fluxo de integração
- **Reservas** valida `turma_id` consultando `GET /turmas/{id}` em **Gerenciamento**.
- **Atividades** valida `turma_id` e `professor_id` consultando `GET /turmas/{id}` e `GET /professores/{id}` em **Gerenciamento**.

## Estrutura de cada microsserviço
Cada serviço possui:
- `models/` (definições SQLAlchemy)
- `controllers/` (funções CRUD de negócios)
- `routes.py` (endpoints REST + docstrings Flasgger)
- `database.py` (inicialização do SQLAlchemy)
- `app.py` (inicializador Flask + Swagger)
- `requirements.txt` e `Dockerfile`

## Testes rápidos (exemplos curl)
1. Criar professor:
```
curl -X POST -H "Content-Type: application/json" -d '{"nome":"Prof A","idade":40,"materia":"Matematica"}' http://localhost:5000/professores
```
2. Criar turma (usando professor_id):
```
curl -X POST -H "Content-Type: application/json" -d '{"descricao":"Turma 1","professor_id":1}' http://localhost:5000/turmas
```
3. Criar reserva (valida turma):
```
curl -X POST -H "Content-Type: application/json" -d '{"num_sala":"101","lab":false,"data":"2025-11-20","turma_id":1}' http://localhost:5001/reservas
```
4. Criar atividade (valida turma e professor):
```
curl -X POST -H "Content-Type: application/json" -d '{"titulo":"Prova 1","descricao":"...", "peso_porcento":30, "data_entrega":"2025-12-01","turma_id":1,"professor_id":1}' http://localhost:5002/atividades
```

## Observações
- Bancos SQLite serão persistidos dentro das pastas dos serviços montadas como volumes (local do host).
- Swagger UI disponível em `/apidocs` para cada serviço.
