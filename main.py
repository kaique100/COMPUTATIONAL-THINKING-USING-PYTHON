lista=[1,5,7,5,5,9,87,4,5]

def encontra_extremos(lista):
    maior = float("-inf")
    menor = float("inf")

    for i in lista:
        if i > maior:
            maior = i

        if i < menor:
            menor = i
    indice_maior = lista.index(maior)
    indice_menor = lista.index(menor)

    return maior, menor, indice_maior, indice_menor

maior,menor,indice_maior,indice_menor = encontra_extremos(lista)
print(f"O maior número é {maior}")
print(f"O indice do maior número é {indice_maior}")
print(f"O menor número é {menor}")
print(f"O indice do menor número é {indice_menor}")

