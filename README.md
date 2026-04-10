# Conversor Universal

[![Python application](https://github.com/guumarques/C14-A/actions/workflows/python-app.yml/badge.svg)](https://github.com/guumarques/C14-A/actions/workflows/python-app.yml)

Aplicação Flask que reúne três módulos de conversão: **monetário**, **numérico** e **temperatura**. Desenvolvida como atividade prática da disciplina **Engenharia de Software** do Inatel, com foco em pipeline CI/CD, testes automatizados e boas práticas de DevOps.

---

## Módulos

| Módulo | Descrição |
|---|---|
| `conversor_monetario.py` | Conversão entre 7 moedas (USD, BRL, EUR, GBP, JPY, ARS, CAD) com taxas fixas |
| `numeros.py` | Conversão entre bases numéricas (decimal ↔ binário, octal, hexadecimal) |
| `temperatura.py` | Conversão entre escalas de temperatura (Celsius ↔ Kelvin ↔ Fahrenheit) |

---

## Como Rodar

```bash
# Clonar o repositório
git clone https://github.com/guumarques/C14-A.git
cd c14-A

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
python -m flask run
```
---
Acesse `http://127.0.0.1:5000` no navegador. Rotas disponíveis:

| Rota | Descrição |
|---|---|
| `/` | Página inicial com links |
| `/moedas` | Lista moedas suportadas |
| `/converter?valor=100&origem=USD&destino=BRL` | Converte moeda |
| `/taxa?origem=USD&destino=BRL` | Consulta taxa de câmbio |
| `/numeros?n=42` | Conversão numérica (binário, octal, hex) |

---

##  Como Rodar os Testes

```bash
# Rodar todos os testes
python -m pytest -v

# Com relatório de cobertura
python -m pytest --cov=. --cov-report=term-missing
```

O projeto possui testes unitários distribuídos em:

| Arquivo | Cobertura |
|---|---|
| `test_conversor_monetario.py` | fluxo normal + fluxo de extensão |
| `test_numeros.py` |  Conversões válidas + entradas inválidas |
| `test_temperatura.py` |  Conversões válidas + valores abaixo do zero absoluto, tipos inválidos |

---

## Pipeline CI/CD

O pipeline roda automaticamente via **GitHub Actions** a cada push/PR na branch `main` e possui 4 jobs:

```
tests ──→ build ──→ deploy
              └──→ notification  (paralelo com deploy)
```

1. **Tests** — Executa os 40 testes em múltiplas versões do Python (3.10 a 3.13) com cobertura
2. **Build** — Lint com flake8 + empacotamento com `python -m build`
3. **Deploy** — Publica automaticamente na Vercel (somente na main)
4. **Notification** — Envia e-mail de sucesso ou falha via SMTP (roda em paralelo com deploy)

Os relatórios de teste e o pacote de build são armazenados como **artifacts** no GitHub Actions.

---

## Secrets 

Para o pipeline funcionar, configure os seguintes secrets no repositório:

| Secret | Uso |
|---|---|
| `VERCEL_TOKEN` | Token de acesso da Vercel |
| `VERCEL_ORG_ID` | ID da organização na Vercel |
| `VERCEL_PROJECT_ID` | ID do projeto na Vercel |
| `MAIL_USERNAME` | E-mail para envio de notificações |
| `MAIL_PASSWORD` | Senha de app do e-mail |
| `MY_EMAIL`, `KAUA_EMAIL`, `LUCAS_EMAIL` | Destinatários das notificações |

---

## Tecnologias

- **Python 3.10+**
- **Flask** — Framework web
- **Pytest** + **pytest-cov** — Testes e cobertura
- **Flake8** — Linting
- **GitHub Actions** — CI/CD
- **Vercel** — Deploy

---

## Integrantes

- Gustavo Marques
- Kauã Victor
- Lucas David

##  Uso de IA

Foi utilizada inteligência artificial como ferramenta de consulta, auxiliando em dúvidas sobre a configuração do pipeline CI/CD e na formatação do README. A lógica do projeto e a estrutura geral foram desenvolvidos pela equipe.