menu = """

> Bem-vindo ao nosso banco!

========== Menu ==========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================

Digite a operação desejada => """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por operação.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    
    elif opcao == "e":
        print("\n==========EXTRATO==========")
        if extrato == " ":
            print("\nNão foram realizadas movimentações.\n")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("===========================")
    
    elif opcao == "q":
        print("""

==========================
                     
Agradecemos a preferência! 
              
Até logo!
              
==========================
              
              """)
        break

    else:
        print("Operação inválida. Por favor selecione a operação desejada.")