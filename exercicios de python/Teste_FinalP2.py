def tabuada(n):
    for i in range(1, n+1):
        print(f"Tabuada do {i}")
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}")
        if i % 20 == 0:
            input("Continuar? (Enter)")

while True:
    print("\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Tabuada\n6-Sair")
    op = int(input("Opção: "))
    if op == 6:
        break
    if op == 5:
        n = int(input("Número até 1000: "))
        if 1 <= n <= 1000:
            tabuada(n)
    else:
        a = float(input("Valor 1: "))
        b = float(input("Valor 2: "))
        if op == 1:
            print("Soma:", a + b)
        elif op == 2:
            print("Subtração:", a - b)
        elif op == 3:
            print("Multiplicação:", a * b)
        elif op == 4:
            if b != 0:
                print("Divisão:", a / b)
            else:
                print("Erro: divisão por zero")
