n = int(input("Digite um número: "))
if n < 2:
    print("Não é primo")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    print("É primo" if primo else "Não é primo")
