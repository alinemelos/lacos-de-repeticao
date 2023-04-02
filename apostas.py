qnt_rodadas = int(input())
nome_play = ''
aposta_play = 0
acertos_estimados = 0
amg_contra = 0
nome_amg = ''
valor = 0
expressao = ''
num_rodada = 1
rodadas = 3
certas = 0
A = ''
F = ''
G = ''
M = ''
A1 = 0
F1 = 0
G1 = 0
M1 = 0
aposta_f = 0
aposta_g = 0
aposta_a = 0
aposta_m = 0

while qnt_rodadas > 0 :
    print(f'Rodada numero {num_rodada}')
    qnt_rodadas -= 1
    num_rodada += 1

    nome_play = str(input())
    print(f'Jogador: {nome_play}')

    aposta_play = int(input())
    print(f'Valor apostado: {aposta_play}')

    acertos_estimados = int(input())
    print(f'Acreditando que acerta {acertos_estimados} vezes em 3 tentativas')

    amg_contra = int(input())
    print(f'{amg_contra} amigos apostaram contra')
    if amg_contra == 3 :
        print(f'Parece que {nome_play} está sendo subestimado!')

    for i in range(amg_contra) :
        nome_amg = str(input())
        valor = int(input())
        print(f'{nome_amg} apostou {valor}')
        if nome_amg == 'Artur' :
            A = 'Artur'
            aposta_a = valor
        elif nome_amg == 'Frej' :
            F = 'Frej'
            aposta_f = valor
        elif nome_amg == 'Guga' :
            G = 'Guga'
            aposta_g = valor
        elif nome_amg == 'Misheldon' :
            M = 'Misheldon'
            aposta_m = valor

    while rodadas > 0 :
        rodadas -= 1
        expressao = str(input())
        if expressao == 'Receba!' :
            certas += 1
        elif expressao != 'Receba!' :
            print(f'Errou! Restam {rodadas} tentativas')
        expressao = ''

    if certas >= acertos_estimados :
        if nome_play == 'Artur' :
            if F == 'Frej' and G == 'Guga' and M == 'Misheldon' :
                A1 += aposta_f + aposta_g + aposta_m
                F1 -= aposta_f
                G1 -= aposta_g
                M1 -= aposta_m
            elif F == 'Frej' and G == 'Guga' :
                A1 += aposta_f + aposta_g
                F1 -= aposta_f
                G1 -= aposta_g
            elif F == 'Frej' and M == 'Misheldon' :
                A1 += F1 + aposta_m
                F1 -= aposta_f
                M1 -= aposta_m
            elif G == 'Guga' and M == 'Misheldon' :
                A1 += aposta_g + aposta_m
                M1 -= aposta_m
                G1 -= aposta_g
            elif F == 'Frej' :
                A1 += aposta_f
                F1 -= aposta_f
            elif G == 'Guga' :
                A1 += aposta_g
                G1 -= aposta_g
            elif M == 'Misheldon' :
                A1 += aposta_m
                M1 -= aposta_m
        elif nome_play == 'Frej' :
            if A == 'Artur' and G == 'Guga' and M == 'Misheldon' :
                F1 += aposta_a + aposta_g + aposta_m
                A1 -= aposta_a
                G1 -= aposta_g
                M1 -= aposta_m
            elif A == 'Artur' and G == 'Guga' :
                F1 += aposta_a + aposta_g
                A1 -= aposta_a
                G1 -= aposta_g
            elif A == 'Artur' and M == 'Misheldon' :
                F1 += aposta_a + aposta_m
                A1 -= aposta_a
                M1 -= aposta_m
            elif G == 'Guga' and M == 'Misheldon' :
                F1 += aposta_g + aposta_m
                M1 -= aposta_m
                G1 -= aposta_g
            elif A == 'Artur' :
                F1 += aposta_a
                A1 -= aposta_a
            elif G == 'Guga' :
                F1 += aposta_g
                G1 -= aposta_g
            elif M == 'Misheldon' :
                F1 += aposta_m
                M1 -= aposta_m
        elif nome_play == 'Guga' :
            if A == 'Artur' and F == 'Frej' and M == 'Misheldon' :
                G1 += aposta_a + aposta_f + aposta_m
                F1 -= aposta_f
                M1 -= aposta_m
                A1 -= aposta_a
            elif A == 'Artur' and F == 'Frej' :
                G1 += aposta_a + aposta_f
                F1 -= aposta_f
                A1 -= aposta_a
            elif A == 'Artur' and M == 'Misheldon' :
                G1 += aposta_a + aposta_m
                A1 -= aposta_a
                M1 -= aposta_m
            elif F == 'Frej' and M == 'Misheldon' :
                G1 += aposta_f + aposta_m
                F1 -= aposta_f
                M1 -= aposta_m
            elif F == 'Frej' :
                G1 += aposta_f
                F1 -= aposta_f
            elif A == 'Artur' :
                G1 += aposta_a
                A1 -= aposta_a
            elif M == 'Misheldon' :
                G1 += aposta_m
                M1 -= aposta_m
        elif nome_play == 'Misheldon' :
            if A == 'Artur' and G == 'Guga' and F == 'Frej' :
                M1 += aposta_a + aposta_g + aposta_f
                F1 -= aposta_f
                G1 -= aposta_g
                A1 -= aposta_a
            elif A == 'Artur' and G == 'Guga' :
                M1 += aposta_a + aposta_g
                A1 -= aposta_a
                G1 -= aposta_g
            elif A == 'Artur' and F == 'Frej' :
                M1 += aposta_a + aposta_f
                F1 -= aposta_f
                A1 -= aposta_a
            elif G == 'Guga' and F == 'Frej' :
                M1 += aposta_g + aposta_f
                F1 -= aposta_f
                G1 -= aposta_g
            elif F == 'Frej' :
                M1 += aposta_f
                F1 -= aposta_f
            elif G == 'Guga' :
                M1 += aposta_g
                G1 -= aposta_g
            elif A == 'Artur' :
                M1 += aposta_a
                A1 -= aposta_a
    else :
        if nome_play == 'Artur' :
            if F == 'Frej' and G == 'Guga' and M == 'Misheldon' :
                F1 += aposta_play
                G1 += aposta_play
                M1 += aposta_play
                A1 -= 3 * aposta_play
            elif F == 'Frej' and G == 'Guga' :
                F1 += aposta_play
                G1 += aposta_play
                A1 -= 2 * aposta_play
            elif F == 'Frej' and M == 'Misheldon' :
                F1 += aposta_play
                M1 += aposta_play
                A1 -= 2 * aposta_play
            elif G == 'Guga' and M == 'Misheldon' :
                G1 += aposta_play
                M1 += aposta_play
                A1 -= 2 * aposta_play
            elif F == 'Frej' :
                F1 += aposta_play
                A1 -= aposta_play
            elif G == 'Guga' :
                A1 -= aposta_play
                G1 += aposta_play
            elif M == 'Misheldon' :
                M1 += aposta_play
                A1 -= aposta_play
        elif nome_play == 'Frej' :
            if A == 'Artur' and G == 'Guga' and M == 'Misheldon' :
                F1 -= 3 * aposta_play
                M1 += aposta_play
                A1 += aposta_play
                G1 += aposta_play
            elif A == 'Artur' and G == 'Guga' :
                A1 += aposta_play
                G1 += aposta_play
                F1 -= 2 * aposta_play
            elif A == 'Artur' and M == 'Misheldon' :
                A1 += aposta_play
                M1 += aposta_play
                F1 -= 2 * aposta_play
            elif G == 'Guga' and M == 'Misheldon' :
                M1 += aposta_play
                G1 += aposta_play
                F1 -= 2 * aposta_play
            elif A == 'Artur' :
                A1 += aposta_play
                F1 -= aposta_play
            elif G == 'Guga' :
                F1 -= aposta_play
                G1 += aposta_play
            elif M == 'Misheldon' :
                M1 += aposta_play
                F1 -= aposta_play
        elif nome_play == 'Guga' :
            if A == 'Artur' and F == 'Frej' and M == 'Misheldon' :
                F1 += aposta_play
                A1 += aposta_play
                M1 += aposta_play
                G1 -= 3 * aposta_play
            elif A == 'Artur' and F == 'Frej' :
                F1 += aposta_play
                A1 += aposta_play
                G1 -= 2 * aposta_play
            elif A == 'Artur' and M == 'Misheldon' :
                A1 += aposta_play
                M1 += aposta_play
                G1 -= 2 * aposta_play
            elif F == 'Frej' and M == 'Misheldon' :
                F1 += aposta_play
                M1 += aposta_play
                G1 -= 2 * aposta_play
            elif A == 'Artur' :
                A1 += aposta_play
                G1 -= aposta_play
            elif F == 'Frej' :
                G1 -= aposta_play
                F1 += aposta_play
            elif M == 'Misheldon' :
                M1 += aposta_play
                G1 -= aposta_play
        elif nome_play == 'Misheldon' :
            if A == 'Artur' and G == 'Guga' and F == 'Frej' :
                F1 += aposta_play
                A1 += aposta_play
                G1 += aposta_play
                M1 -= 3 * aposta_play
            elif A == 'Artur' and G == 'Guga' :
                G1 += aposta_play
                A1 += aposta_play
                M1 -= 2 * aposta_play
            elif A == 'Artur' and F == 'Frej' :
                F1 += aposta_play
                A1 += aposta_play
                M1 -= 2 * aposta_play
            elif G == 'Guga' and F == 'Frej' :
                F1 += aposta_play
                G1 += aposta_play
                M1 -= 2 * aposta_play
            elif A == 'Artur' :
                A1 += aposta_play
                M1 -= aposta_play
            elif G == 'Guga' :
                M1 -= aposta_play
                G1 += aposta_play
            elif F == 'Frej' :
                F1 += aposta_play
                M1 -= aposta_play
    A = ''
    F = ''
    G = ''
    M = ''
    aposta_a = 0
    aposta_f = 0
    aposta_g = 0
    aposta_m = 0
    rodadas = 3

else :
    print(f'Fim de jogo, o resultado foi:')
    print(f'Artur ficou com {A1} de saldo')
    print(f'Frej ficou com {F1} de saldo')
    print(f'Guga ficou com {G1} de saldo')
    print(f'Misheldon ficou com {M1} de saldo')
