primos = []
num = 2
while len(primos) < 10:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primos.append(num)
    num += 1
print(primos)
