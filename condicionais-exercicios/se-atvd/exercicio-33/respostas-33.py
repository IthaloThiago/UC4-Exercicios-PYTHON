idade = input("Digite sua idade")

if idade >=5 and idade <= 10:
    print("Infantil")
elif idade >=11 and idade <= 14:
    print("Juvenil")
elif idade >=15 and idade <= 17:
    print("Cadete")
elif idade >=18 and idade <= 35:
    print("Profissional")
else:
    print("Master")