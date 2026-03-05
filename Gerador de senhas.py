import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tamanho = int(input("Digite o tamanho da sua senha: "))
senhagerada = ""

for i in range(tamanho):
    senhagerada += random.choice(caracteres)
print("Senha gerada:", senhagerada)
