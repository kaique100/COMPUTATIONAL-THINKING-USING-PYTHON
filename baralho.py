import random

def cria():
    lista = []

    for valor in range(1,14):
        lista.append((valor, 'P'))
        lista.append((valor, 'C'))
        lista.append((valor, 'E'))
        lista.append((valor, 'O'))

    return lista

def compra(deck):
    if len(deck) == 0:
        raise Exception("Baralho vazio")
    return deck.pop(0)

def distribui(deck, qtd):
    mao = []
    while qtd > 0:
        c = compra(deck)
        mao.append(c)
        qtd = qtd - 1
    return mao

def embaralha(deck):

    for k in range(200):
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux

