

print(">>>>>>>=== ATIVIDADES DO GPT PARA PRATICAR !! ===<<<<<<<")


print("##################################################################")
print("##################################################################")

###################################
#Atividade — Caixa de supermercado
###################################


print(">>>>>>>=== Caixa de Supermercado ===<<<<<<<")    

nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))


resultado = preco_produto * quantidade_produto


print(f"O total para {nome_produto} é: R$ {resultado:.2f}")

if preco_produto >= 100:
    desconto = resultado * 0.10
    print(" ===== CUPOM DE 10% =====")
    total_com_desconto = resultado - desconto
    print(f"O total com desconto para {nome_produto} é: R$ {total_com_desconto:.2f}")

elif preco_produto < 100:
    print(f"O total sem desconto para {nome_produto} é: R$ {resultado:.2f}")

else:
    print("SEM DESCONTO.")


print("........................................................")
print("........................................................")
print("........................................................")


#########################################
#Atividade — Sistema de caixa eletrônico
#########################################


print("===== SISTEMA DE CAIXA ELETRÔNICO =====")

nome_usuario = input("Digite o nome do usuário: ")
saldo_atual = float(input("Digite o saldo atual: R$ "))

print("1 - Consultar saldo")
print("2 - Depósito")
print("3 - Saque")
print("4 - Sair")

opcao = int(input("Escolha uma opção: "))


match opcao:
    case 1:
        print(f"Olá, {nome_usuario}!")
        print(f"Saldo atual: R$ {saldo_atual:.2f}")

    case 2:
        deposito = float(input("Digite o valor do depósito: R$ "))

        if deposito > 0:
            saldo_atual += deposito
            print(f"Saldo após depósito: R$ {saldo_atual:.2f}")
        else:
            print("Valor de depósito inválido!")

    case 3:
        saque = float(input("Digite o valor do saque: R$ "))

        if saque <= 0:
            print("Valor de saque inválido!")
        elif saque <= saldo_atual:
            saldo_atual -= saque
            print(f"Saldo após saque: R$ {saldo_atual:.2f}")
        else:
            print("Saldo insuficiente para saque!")

    case 4:
        print("Obrigado por utilizar o sistema!")

    case _:
        print("Opção inválida!")

print("OBRIGADO POR UTILIZAR O SISTEMA DE CAIXA ELETRÔNICO!")



print("........................................................")
print("........................................................")
print("........................................................")

