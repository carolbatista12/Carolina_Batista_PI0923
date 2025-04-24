for i in range(0, 256, 20):
    for j in range(i, min(i+20, 256)):
        print(f"{j} -> {chr(j)}")
    input("Continuar? (Enter)")
