# variaveis basicas
palavra = ''
acao = 0
resposta = ''

gabarito = ''
vida_calegario = 3
vida_apostador = 3

perdedor = ''
vencedor = ''

while vida_apostador > 0 and vida_calegario > 0 :
    palavra = str(input())
    acao = int(input())
    resposta = str(input())
    if acao == 1 :
        # tras pra frente
        for i in palavra :
          gabarito = i + gabarito
    elif acao == 2 :
        # palavra em binario
        gabarito = ''.join('{0:08b}'.format(ord(x), 'b') for x in palavra)
    
    if gabarito == resposta :
        vida_apostador -= 1
        perdedor += 'apostador'
        print(f'Rodada Concluída!')
        print(f'{perdedor} perdeu uma vida')
    elif gabarito != resposta :
        vida_calegario -= 1
        perdedor += 'calegario'
        print(f'Rodada Concluída!')
        print(f'{perdedor} perdeu uma vida')

    if perdedor != 'calegario' and acao == 2 :
        print('Como alguém consegue fazer isso de cabeça?')

    perdedor = ''
    palavra = ''
    acao = 0
    gabarito = ''
else :
    print('Partida Concluída!')
    if vida_apostador == 0 :
        vencedor += 'calegario'
        print(f'Vencedor: {vencedor}')
        print('Droga, não acredito que eu perdi essa partida, achei que seria uma vitória fácil...')
    elif vida_calegario == 0 :
        vencedor += 'apostador'
        print(f'Vencedor: {vencedor}')
        print('HAHAHA, acha mesmo que preciso trapacear para ganhar de você?')