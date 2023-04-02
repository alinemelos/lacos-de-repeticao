letra = str(input())
qnt_amigos = int(input())
estado_fav = str(input())
nome = ''
estado_amg = ''
contagem = 0
controle = 0
local_ganhador = ''
dias = 0

while qnt_amigos > 0 :
    nome = str(input())
    estado_amg = str(input())
    qnt_amigos -= 1
    for i in estado_amg:
        if i == letra:    # vai checar se a palavra tem a letra digitada
          contagem += 1          # vai dizer quantas letras tem
    if contagem > controle :
        controle = contagem
        local_ganhador = estado_amg
        dias = contagem
    elif contagem < controle :
        dias = controle
    contagem = 0

if local_ganhador == estado_fav :
    print(f'UHUL!!! Victor vai começar por {local_ganhador} que é o estado que ele queria e ficara la por {dias} dias.')
else :
    print(f'Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado {local_ganhador} e ficara la por {dias} dias.')
