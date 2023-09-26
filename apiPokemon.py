import requests
import pprint


print(4 * "\n")
print(50 * "=")
print(10 * " ", "Trabalhando com o pokéAPI")
print(50 * "=")
print()

url ="https://pokeapi.co/api/v2/berry/1/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    pprint.pprint(data)
else:
    print("Falha na solicitaçã. Código de status:", response.status_code)
