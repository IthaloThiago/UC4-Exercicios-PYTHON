consumo = float(input("Digite o consumo de energia em kWh: "))

if consumo > 200:
    consumo = consumo + 25

print("Consumo atualizado:", consumo, "kWh")
