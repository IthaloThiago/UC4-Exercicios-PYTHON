livros = int(input("Digite a quantidade de livros comprados: "))
jogos = int(input("Digite a quantidade de jogos comprados: "))
valor = float(input("Digite o valor total da compra: R$ "))

if livros >= 2 or jogos >= 3:
    valor = valor - 25

print("Valor final da compra: R$", valor)
