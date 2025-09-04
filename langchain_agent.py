from fastapi import FastAPI, Body
from pydantic import BaseModel, constr
from langchain_community.llms import AzureChatOpenAI

app = FastAPI()

class CodeInput(BaseModel):
    code: constr(min_length=1)

# Configurar LangChain com Azure OpenAI
llm = AzureChatOpenAI(
    deployment_name="gpt35turbo16k", 
    model_name="gpt-35-turbo",
    temperature=0,
)

@app.post("/generate-test")
async def generate_test(input: CodeInput = Body(..., example={
    "code": "def soma(a, b):\n    return a + b"
})):
    prompt = f"""
Você é um assistente que gera testes unitários para o código Python dado.

Código:
{input.code}

Gere um teste unitário simples para essa função.
"""
    # Como é um chat, o prompt deve ser passado como lista de mensagens
    messages = [{"role": "user", "content": prompt}]
    response = llm.generate(messages)
    
    # response gera uma lista de GenerationResult, pegar o texto
    test_code = response.generations[0][0].text

    return {"test_code": test_code}
