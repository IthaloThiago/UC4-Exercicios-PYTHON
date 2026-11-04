
jogos = int(input("Digite a quantidade de jogos comprados: "))
compra = float(input("Digite o valor total da compra: R$ "))
pontos = int(input("Digite a pontuação inicial do cliente: "))

if jogos >= 3 and compra > 500:
    pontos = pontos + 200

print("Pontuação final:", pontos)
