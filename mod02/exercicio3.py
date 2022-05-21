# --------COMEÇO DA FUNÇÃO DIMENSAOTRANSPORTE----------
def dimensaoT():
    while True:
        try:
            comprimentoT = float(
                input("Digite o comprimento do objeto (em cm): "))
            alturaT = float(input("Digite a altura do objeto (em cm): "))
            larguraT = float(input("Digite o largura do objeto (em cm): "))
        except ValueError:
            print("Você digitou alguma dimensão do objeto com valor não numérico, \npor favor entre com as dimensões desejados novamente.")
            continue

        volumeT = comprimentoT * alturaT * larguraT
        print("O volume do objeto é (em cm³):{:.2f}".format(volumeT))

        if 0 <= volumeT < 1000:
            return 10
        elif 1000 <= volumeT < 10000:
            return 20
        elif 10000 <= volumeT < 30000:
            return 30
        elif 30000 <= volumeT <= 100000:
            return 50
        else:
            print("Não aceitamos objetos com dimensões tão grandes. Tente novamente")
            continue


# --------FIM DA FUNÇÃO DIMENSAOTRANSPORTE----------
# --------COMEÇO DA FUNÇÃO PESOTRANSPORTE----------
def pesoT():
    while True:
        try:
            pesoT = float(input("Digite o peso do objeto (em Kg): "))
            if 0 < pesoT <= 0.1:
                return 1
            elif 0.1 < pesoT <= 1:
                return 1.5
            elif 1 < pesoT <= 10:
                return 2
            elif 10 < pesoT <= 30:
                return 3
            else:
                print("Não aceitamos objetos tão pesados. Tente novamente")
                continue
        except ValueError:
            print("Você digitou um peso com valor não numérico. Tente novamente")
            continue

# --------FIM DA FUNÇÃO PESOTRANSPORTE----------
# --------COMEÇO DA FUNÇÃO ROTATRANSPORTE----------


def rotaT():
    while True:
        rotaT = input("Selecione a rota desejada: \nRS - De Rio de Janeiro até São Paulo \nSR - De São Paulo até Rio de Janeiro \nBS - De Brasília até São Paulo \nSB - De São Paulo até Brasília \nBR - De Brasília até Rio de Janeiro \nRB - De Rio de Janeiro até Brasília \n>>")
        if rotaT == "RS":
            return 1
        if rotaT == "SR":
            return 1
        if rotaT == "BS":
            return 1.2
        if rotaT == "SB":
            return 1.2
        if rotaT == "BR":
            return 1.5
        if rotaT == "RB":
            return 1.5
        else:
            print("Você digitou uma rota que não exite. Tente novamente")
            continue
# --------FIM DA FUNÇÃO ROTATRANSPORTE----------

# --------COMEÇO DA MAIN----------


print("Bem-vindo a Transportadora Felipe de Moraes Rodrigues")

dimensao = dimensaoT()
peso = pesoT()
rota = rotaT()
total = dimensao * peso * rota
print("O valor total foi de: R$ {:.2f}" . format(total))

# --------FIM DA MAIN----------
