temperatura = float(input("Digite a temperatura atual em °C: "))
if temperatura > 35:
    temperatura_final = temperatura + 5
else:
    temperatura_final = temperatura

print(f"A temperatura final é: {temperatura_final:.1f} °C")