# TDD com LangChain e Azure ChatGPT

Este projeto demonstra como automatizar a criação de testes unitários usando LLMs via LangChain com Azure OpenAI, integrados com uma API FastAPI.

## 🚀 Funcionalidade

- Recebe uma função Python como entrada
- Retorna um teste unitário correspondente, gerado pela LLM (ChatGPT da Azure via LangChain)

## 🛠 Tecnologias

- Python
- FastAPI
- LangChain
- Azure OpenAI
- Uvicorn
- Requests
- .env + python-dotenv

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/TDD_LangchainChatGPT.git
cd TDD_LangchainChatGPT
pip install -r requirements.txt

Crie um arquivo .env com:
AZURE_OPENAI_API_KEY=xxxxxxxxxxxx
AZURE_OPENAI_ENDPOINT=https://xxxxxx.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-07-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt35turbo16k


▶️ Executando

uvicorn app.langchain_agent:app --reload



📩 Exemplo de Requisição

POST /generate-test
```
{
  "code": "def soma(a, b):\n    return a + b"
}
```



Resposta:

```
{
  "test_code": "def test_soma():\n    assert soma(2, 3) == 5\n    assert soma(-1, 1) == 0"
}
```



✅ Resultado Esperado

Testes unitários gerados dinamicamente para funções Python simples.



💡 Melhorias Futuras

Adicionar suporte para múltiplas funções no mesmo input

Melhorar o prompt para gerar testes com pytest

Validação automática dos testes gerados
