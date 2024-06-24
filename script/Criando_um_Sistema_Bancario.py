menu = '''
    Bem Vindo, selecione à opção desajada.

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

    => '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor_deposito = float(input('informe o valor a ser depositado: '))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'   Depósito: R$ {valor_deposito:17.2f} (+)\n'
            print(f'Deposito de R$ {valor_deposito:.2f} realizado com sucesso!')
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == '2':
        if numero_saques < LIMITE_SAQUES:
            valor_sacado = float(input('informe o valor a ser sacado: '))

            if valor_sacado > 0:
                if valor_sacado <= limite:
                    if valor_sacado <= saldo:
                        saldo -= valor_sacado
                        numero_saques += 1
                        extrato += f"   Saque:    R$ {valor_sacado:17.2f} (-)\n"
                        print(f'Saque de R$ {valor_sacado:.2f} realizado com sucesso!')
                    else:
                        print('Operação falhou! Saldo insuficiente para saque.')
                else:
                    print('Operação falhou! Valor solicitado acima do limite de saque de R$ 500,00.')
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print(f'Operação falhou! Ultrapassado o limite de {LIMITE_SAQUES} saques diários.')

    elif opcao == '3':
        print('\n            Extrato Bancário')
        print('=' * 40)
        print('   Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n   Saldo:    R$ {saldo:17.2f}')
        print(f'\n   Numero de Saques: {numero_saques:12}')
        print('=' * 40)

    elif opcao == '0':
        print('  Obrigado por utilizar os nossos serviços!')
        break

    else:
        print('Opção selecionada incorreta, seleciona a opção correta.')
