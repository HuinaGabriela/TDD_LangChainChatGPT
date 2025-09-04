from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/generate-test")
async def generate_test(code: str = Body(..., example="def soma(a, b):\n    return a + b")):
    test_code = f"""def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
"""
    return {"test_code": test_code}

