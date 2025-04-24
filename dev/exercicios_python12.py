n = int(input("Quantos números? "))
soma = sub = mult = div = 0
for i in range(1, n):
    soma += n + i
    sub += n - i
    mult += n * i
    if i != 0:
        div += n / i
print("Operações efetuadas:", (n-1)*4)
