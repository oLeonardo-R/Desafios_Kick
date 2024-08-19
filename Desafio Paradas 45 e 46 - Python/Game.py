import random

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    
    if jogador not in opcoes:
        print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
        return
    
    computador = random.choice(opcoes)
    
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")
    
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
jogar_pedra_papel_tesoura()