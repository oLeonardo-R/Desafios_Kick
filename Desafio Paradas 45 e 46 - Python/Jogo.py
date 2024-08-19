import random

def jogar_pedra_papel_tesoura():
    # Lista de opções disponíveis
    opcoes = ["pedra", "papel", "tesoura"]
    
    # Solicita a escolha do jogador
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    
    # Verifica se a escolha do jogador é válida
    if jogador not in opcoes:
        print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
        return
    
    # Gera a escolha aleatória do computador
    computador = random.choice(opcoes)
    
    # Mostra as escolhas
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")
    
    # Determina o vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

# Chama a função para iniciar o jogo
jogar_pedra_papel_tesoura()