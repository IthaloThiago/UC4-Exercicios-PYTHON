valor_compra = int(input("Digite o valor total da compra: "))
if valor_compra > 200:
    valor_final = valor_compra - 30
else:
    valor_final = valor_compra

print(f"O valor a pagar é: R$ {valor_final:.2f}")
    



