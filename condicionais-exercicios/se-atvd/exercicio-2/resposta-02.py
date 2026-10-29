salario = float(input("Digite o salário do funcionário: "))
if salario < 1500:
    salario_final = salario + 200
else:
    salario_final = salario

print(f"O valor final do salário é: R$ {salario_final:.2f}")