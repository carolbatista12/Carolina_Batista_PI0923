clientes = []
idcli = 1

while True:
    print("\n1-Inserir\n2-Listar\n3-Buscar\n4-Sair")
    op = int(input("Opção: "))
    if op == 4:
        break
    elif op == 1:
        nome = input("Nome: ")
        morada = input("Morada: ")
        tel = input("Tel: ")
        nif = input("NIF: ")
        compra = float(input("Valor da compra: "))
        if compra < 100:
            desconto = 0
        elif compra <= 200:
            desconto = 0.05
        elif compra <= 500:
            desconto = 0.10
        else:
            desconto = 0.15
        divfin = compra - (compra * desconto)
        cliente = {
            'id': idcli,
            'nome': nome,
            'morada': morada,
            'tel': tel,
            'nif': nif,
            'compra': compra,
            'divfin': divfin
        }
        clientes.append(cliente)
        idcli += 1
    elif op == 2:
        for cli in clientes:
            print(cli)
            input("Próximo? (Enter)")
    elif op == 3:
        busca = int(input("Digite o número do cliente: "))
        for cli in clientes:
            if cli['id'] == busca:
                print(cli)
                break
        else:
            print("Cliente não encontrado")
