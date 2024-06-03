menu = """ 
    Seja bem vindo ao Banco ProgramatorX123;

    [0]- Depositar;
    [1]- Sacar;
    [2]- Extrato;
    [9]- Sair;

"""
valorDeposito = 0
valorSaque = 0
saldo = 0
limite = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE_DIARIO = 500

while True:

    opcao = input(menu)
    
    if opcao == "0":
        print("Depósito selecionado!")
        valorDeposito = int(input("Digite o valor para depositar: "))
        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print("Depósito realizado!")
        else:
            print("Erro no depósito!")

    elif opcao == "1":
        print("Saque selecionado! ")
        if numero_saques < LIMITE_SAQUES:
            valorSaque = int(input("Digite o valor para sacar: "))
            if valorSaque > 0 and valorSaque <= saldo and valorSaque <= LIMITE_SAQUE_DIARIO:
                saldo -= valorSaque
                extrato += f"Saque: R$ {valorSaque:.2f}\n"
                numero_saques += 1
                print("Saque realizado!")
            else:
                print("Erro no saque!")
        else:
            print("Limite diário de saque alcançado!")

    elif opcao == "2":
        print("Extrato selecionado!")
        print(extrato)
        print(f"Saldo: {saldo:.2f}")

    elif opcao == "9":
        print("Saindo!")
        break
    else:
        print("Operação inválida")

