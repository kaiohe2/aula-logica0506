taxa_brl_para_usd = 5.29 # 1 USD = 5.29 BRL
taxa_usd_para_brl = 1 / taxa_brl_para_usd # 1 BRL =0.20 USD

while True:
    #Exibe o meu opeções
    print("\n escolha uma opção:")
    print("1. BRL para US$")
    print("2 us$ para BRL")
    print("3. sair")

    opçao = input("digite o numero da opeção desejada")

    if opçao == '1' :
        valor_brl = float(input("dgite o valor em (R$): "))
        valor_usd = valor_brl / taxa_brl_para_usd
        print(f"R$ { valor_usd:.2f} é equivalente a uS$ {valor_usd:.2f}")
    elif opçao == '2':
        valor_usd = float(input("digite o valor em dolares (US$)"))
        valor_brl = valor_usd * taxa_brl_para_usd
        print(f"US$ {valor_usd:.2f} é equivalente a R$ {valor_usd:.2f}")
    elif opçao == '3':
        print("saindo...")
        break
    else:
        print("opção inválida.. tente novamente.")
        