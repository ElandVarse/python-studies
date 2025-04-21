import random

print("🎲 Bem-vindo ao jogo do Adivinha o Número!")
print("Pensei em um número de 1 a 100. Tente adivinhar!")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = input("Digite seu palpite: ")
    
    # Verifica se é número
    if not tentativa.isdigit():
        print("Digite apenas números, por favor!")
        continue

    tentativa = int(tentativa)
    tentativas += 1

    if tentativa < numero_secreto:
        print("🔼 Muito baixo!")
    elif tentativa > numero_secreto:
        print("🔽 Muito alto!")
    else:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break
