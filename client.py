import requests

res = requests.get("http://127.0.0.1:8000/sample")

print(res.status_code)
print(res.text)
