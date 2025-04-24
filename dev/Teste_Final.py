def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def divisores(n):
    return [i for i in range(1, n+1) if n % i == 0]
def perfeito(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
n = int(input("Digite um número (1 a 30000): "))
if 1 <= n <= 30000:
    for i in range(n, 0, -1):
        print(f"Número: {i}")
        print("Primo?" , eh_primo(i))
        print("Divisores:", len(divisores(i)))
        print("Perfeito?", perfeito(i))
        if i % 10 == 0:
            cont = input("Parar? (s/n): ")
            if cont == 's':
                break
