# Agenda de Serviços

API REST para agendamento de serviços, pensada para pequenos negócios e profissionais autônomos. Permite cadastrar serviços, marcar horários e evitar conflitos de agenda.

## Status

Em desenvolvimento. A primeira versão tem a rota de verificação da API funcionando.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite (PostgreSQL planejado)
- pytest

## Como rodar

1. Clone o repositório: 
git clone https://github.com/edithgar/agenda-servicos.git
cd agenda-servicos
2. Crie e ative o ambiente virtual:
python -m venv venv
.\venv\Scripts\Activate.ps1
4. Rode o servidor:
python -m uvicorn app.main:app --reload
5. Acesse `http://127.0.0.1:8000` ou a documentação em `http://127.0.0.1:8000/docs`.

## Próximos passos

- Modelos de serviços, clientes e agendamentos
- Regra para impedir agendamentos no mesmo horário
- Testes automatizados com pytest
- Interface simples em HTML, CSS e JavaScript