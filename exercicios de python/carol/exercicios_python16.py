soma = count = 0
while count < 30:
    num = int(input("Digite número par entre 1 e 50: "))
    if 1 <= num <= 50 and num % 2 == 0:
        soma += num
        count += 1
print("Média:", soma / 30)
