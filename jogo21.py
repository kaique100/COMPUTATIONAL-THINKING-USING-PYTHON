import baralho as bar

def quer_carta(mao):
    linha = ""
    for c in mao:
        if c[0] == 1:
            linha = linha + "A"
        elif c[0] == 11:
            linha = linha + "J"
        elif c[0] == 12:
            linha = linha + "Q"
        elif c[0] == 13:
            linha = linha + "K"
        else:
            linha = linha + f"{c[0]}"
    print("Mao " + linha + " ")
    resp = input("Quer amis carta (s/n)?")
    return resp == 's'

def soma(mao):
    pontos = 0 
    for c in mao:
        if c[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + c[0]
    return pontos

def quer_carta_cpu(mao):
    pt = soma(mao)
    if pt < 16:
        return True
    else:
        return False

monte = bar.cria()
bar.embaralha(monte)
# print(monte)

mao_jog = bar.distribui(monte, 2)
mao_cpu = bar.distribui(monte, 2)

while quer_carta(mao_jog):
    c = bar.compra(monte)
    mao_jog.append(c)

while quer_carta_cpu(mao_cpu):
    c = bar.compra(monte)
    mao_cpu.append(c)

print("Pontos Humano", soma(mao_jog))
print("Pontos CPU", soma(mao_cpu))