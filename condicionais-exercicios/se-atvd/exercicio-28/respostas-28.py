ano = int(input("Digite seu ano de nascimento: "))

if ano - 2026 >= 18:
    print("Voce e obrigado a votar")
elif ano - 2026 >= 70:
    print("Voce não e obrigado a vota")
else:
    print("Voce não pode votar")