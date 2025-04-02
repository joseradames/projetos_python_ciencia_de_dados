menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_deposito = float(input("Digite o valor que do depósito: "))

        if valor_deposito <= 0:
              print("Valor digitado não é positivo!" "Reinicie a operação!")

        elif valor_deposito > 0:
            saldo += valor_deposito
            extrato += str(f" R$ {valor_deposito:.2f}\n")
            print(saldo)
            print(extrato)
                  #teste
    elif opcao == "s":
        print("Saque")

        if saldo == 0:
             print("Saldo insuficiente para realizar saque!")

        elif saldo != 0:
                
                if numero_saques != LIMITE_SAQUES:
                
                    valor_saque = float(input("Digite o valor que do saque: "))
            
                    if valor_saque < 0:
                       print("Valor digitado não é positivo!" "Reinicie a operação!")
                
                    elif valor_saque > limite:
                      print("Limite de saque excedido, valor máximo R$ 500.00")

                    elif valor_saque <= limite:
                        saldo -= valor_saque
                        extrato += str(f" - R$ {valor_saque:.2f}\n")
                        numero_saques +=1
                
                else:
                    print("Número de saques excedidos, tente outra operação!")
        

    elif opcao == "e":
        print("Extrato")

        if extrato == "":
            print("Não existem movimentações!")
        
        else:
            
            print(extrato)
            print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida por favor sselecione novamente a operação!")
