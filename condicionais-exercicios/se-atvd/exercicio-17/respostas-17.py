reproducoes = int(input("Digite o numero de reproducoes: "))
curtidas = int(input("Digite a quantidade de curtidas: "))
valor = float(input("Digite o valor ja arrecadado: R$ "))

if reproducoes > 1000 or curtidas > 200:
    valor = valor + 150

print("Valor final arrecadado: R$", valor)
