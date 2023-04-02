acao = str(input())
protetor = 'sem'
carteira = float(0)
clima = 'ensolarado'
comando_final = ''
continua = True
dinheiro = float(0)

#vai fazer enquanto não for para a praia
while acao != 'ir para a praia' :
    #casos até chegar o comando da praia
    if acao == 'separar dinheiro' :
        carteira = float(input())
        dinheiro += carteira
    elif acao == 'passar protetor' :
        protetor = 'passar protetor'
    elif acao == 'choveu' :
        clima = 'chuvoso'
    elif acao == 'parou de chover':
        clima = 'ensolarado'
    else :
        continua = True
    acao = str(input())

#vai para a praia e checar alguns casos
else :
    if protetor != 'passar protetor' and dinheiro < 10.0 and clima == 'ensolarado':
        print('Hoje tem sol e mar!')
        print('Você não chegou muito bem, chame um médico!')
    elif protetor != 'passar protetor' and dinheiro >= 10.0 and clima == 'ensolarado':
        print('Hoje tem sol e mar!')
        print('O novo camarão do CIn foi criado')
    elif protetor == 'passar protetor' and dinheiro < 10.0 and clima == 'ensolarado':
        print('Hoje tem sol e mar!')
        print ('Só faltou uma aguinha de coco...')
    elif protetor == 'passar protetor' and dinheiro >= 10.0 and clima == 'ensolarado':
        print('Hoje tem sol e mar!')
        print('Aí sim! Hoje rendeu!')
    elif clima == 'chuvoso' :
        print('Hoje não vai dar pra ir, chuvinha barrou')

