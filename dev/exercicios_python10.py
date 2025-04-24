n = int(input("Digite um número: "))
divisores = 0
for i in range(1, n+1):
    if n % i == 0:
        divisores += 1
print("Divisores:", divisores)
