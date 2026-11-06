num1 = int(input("Digite a quantidade de maça que voce quer comprar: "))

if num1 < 12:
    print(f"O valor total das maçãs deu {num1 * 1.30}")
else:
     print(f"O valor total das maçãs deu {num1 * 1.25}")