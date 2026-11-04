estoque = int(input("Digite a quantidade em estoque: "))
if estoque <= 20:
    estoque_final = estoque + 50
else:
    estoque_final = estoque

print(f"A quantidade atualizada do estoque é: {estoque_final}")