pontuacao = int(input("Digite a pontuação do jogador: "))
if pontuacao >= 500:
    pontuacao_final = pontuacao + 100
else:
    pontuacao_final = pontuacao

print(f"A pontuação final é: {pontuacao_final}")