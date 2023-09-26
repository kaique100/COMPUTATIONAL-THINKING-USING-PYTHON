import requests
import pprint


url ="https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(4 * "\n")
print(50 * "=")
print(10 * " ", "Trabalhando com GET na API jsonplaceholder")
print(50 * "=")
print()


if response.status_code == 200:
    data = response.json()

    pprint.pprint(data)
else:
    print("Falha na solicitaçã. Código de status:", response.status_code)
