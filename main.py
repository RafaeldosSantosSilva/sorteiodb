import random

db = {"Cliente": [],
      "Produto": [],
      "Valor" : []}

print('---MENU LOJA---')
while True:
    print('Escolha uma opção:')
    print('1. Nova compra')
    print('2. Visualizar Estado Atual')
    print('3. Encerrar Expediente')
    op = input('Digite a opção desejada: ')

    match op:
        case '1':
            cliente = input('Digite o Nome do Cliente: ')
            db['Cliente'].append(cliente)

            produto = input('Digite o Produto Desejado: ')
            db['Produto'].append(produto)

            valor = float(input('Digite o Valor do Produto: '))
            db['Valor'].append(valor)
            print('')
                       
        case '2':
            for clientes, produtos,valores in zip(db['Cliente'],db['Produto'],db['Valor']):
                print(f"Clientes : {clientes}")
                print(f"Produtos : {produtos}")
                print(f"Valores : {valores}")
                print('')
            print('')
        case '3':
            zip_compras = zip(db["Cliente"],db["Produto"],db["Valor"])

            lista_compras = list(zip_compras)

            sorteado = random.choice(lista_compras)

            print(f'O Sorteado foi: {sorteado}')
            break
            
        case _:
            print('Opção inválida! Tente Novamente!')
            print('')
    
