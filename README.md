# LangChain com ChatGPT — Automação de Testes Unitários

## Objetivo
Automatizar a criação de testes unitários usando LLM com LangChain, integrando com Azure e OpenAI.

## Stack & Ferramentas
- **LangChain** (com `langchain-openai`)
- **FastAPI** para API
- **Azure Free Services** (Functions, DevOps) para deploy gratuito  
- **OpenAI (API gratuita)** para geração de testes

## Fluxo do Projeto
1. Cliente envia código-fonte via API.
2. LangChain, usando ChatGPT, gera esqueleto de testes unitários.
3. API retorna os testes prontos em JSON.
4. Deploy contínuo em Azure Functions / App Service.

## Instalação & Configuração
```bash
pip install langchain openai fastapi uvicorn
