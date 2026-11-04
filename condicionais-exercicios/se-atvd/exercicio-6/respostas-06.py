valor_transferencia = float(input("Digite o valor da transferência: "))
if valor_transferencia >= 1000:
    valor_total = valor_transferencia + 15
else:
    valor_total = valor_transferencia

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")