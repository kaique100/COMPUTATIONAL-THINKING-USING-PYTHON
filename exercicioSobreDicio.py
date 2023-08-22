ex = "{'Nome': 'Fulano', 'Curso': 'TDS', 'RM': 1'}"
quebra = ex.split(",")
for i in quebra:
    if i == quebra[0]:
        #opção 1:
        # print(i.split("{")[-1])
        # opção2
        print(i[1:-1].split(":"))
        chave = i[1:].split(":")[0]
        valor = i[1:].split(":")[1]

        dicionario_linha[chave] = valor
    elif i == quebra[-1]:
        print(i.split("}")[0].split(":"))
        # print(i[:-1])
    else:print(i.split(":"))
