import requests

response = requests.get("http://localhost:8080/name")
print(response.status_code)
print(response.text)