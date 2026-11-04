compra = float(input("Digite o valor total da compra: R$ "))

if compra > 150:
    compra = compra - 30

print("Valor que o cliente deverá pagar: R$", compra)
