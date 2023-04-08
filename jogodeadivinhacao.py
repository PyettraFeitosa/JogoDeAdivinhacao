from random import randint

num_secreto = randint(1,1000)

tentativas = 0 

while True:
    tentativa = int(input("Adivinhe o número secreto entre 1 e 1000: "))
    tentativas += 1

    if tentativa < num_secreto:
        print("O número secreto é maior!")
    
    elif tentativa > num_secreto:
        print("O número secreto é menor!")

    else:
        print(f"Você acertou o número secreto em {tentativas} tentativas!")
        break

