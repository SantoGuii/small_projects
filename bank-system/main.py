# Developer: Guilherme dos Santos
# Date: 26-05-2023
# Version: 1.0

# Purpose: Bank system
# description: Sistema bancário com as opções de depósito, saque, extrato e sair

# Menu do sistema bancário
menu = """\n=== Sistema bancário ===
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
Escolha uma opção:
"""

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 3

# Loop infinito do menu do sistema bancário
while True:
    opcao = int(input(menu))

    # Depósito
    if opcao == 1:
        print("\n↪ Para retornar ao menu anterior digite 0")
        valor = float(input("\nDigite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {valor}\n"

        else:
            pass

    # Saque
    if opcao == 2:
        if numero_saques > 0:
            print("\n↪ Para retornar ao menu anterior digite 0")
            print(f"\nSaques disponíveis: {numero_saques}")
            valor = float(input("Digite o valor do saque: "))
            if valor > 0:
                if valor <= saldo:
                    if valor <= limite:
                        saldo -= valor
                        extrato += f"Saque: {valor}\n"
                        numero_saques -= 1
                    else:
                        print("Limite excedido")
                else:
                    print("Saldo insuficiente")
            else:
                pass

    # Extrato
    if opcao == 3:
        print("\n↪ Para retornar ao menu anterior digite 0")
        print("\n=== Extrato ===")
        print(f"\nSaldo: {saldo}")
        print(f"Limite: {limite}")
        print(f"Saques disponíveis: {numero_saques}")
        print(f"\nMovimentações:\n{extrato}")

    # Sair
    if opcao == 4:
        break