import requests

url = "http://127.0.0.1:8000/generate-test"
payload = {
    "code": "def soma(a, b):\n    return a + b"
}
response = requests.post(url, json=payload)
print(response.json())
