# variaveis 
nome_invencao = str(input())
# variáveis das etapas
nome_etapa = ''
custo_etapa = 0
tentativas = 0
status = ''
# variavel de controle
seguir = True 
#variaveis de contagem
total_correto = 0
total_falhas = 0
etapas_feitas = 0
total_gasto_etapa = 0
total_invencao = 0

while seguir == True :
    nome_etapa = str(input())
    if nome_etapa == 'concluir' or nome_etapa == 'desistir' :
        seguir = False
    elif nome_etapa == 'dar um plus' :
        custo_etapa = int(input())
        print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')
        total_gasto_etapa += custo_etapa
    else :
        custo_etapa = int(input())
        tentativas = int(input())
        while tentativas > 0 :
            tentativas -= 1
            status = str(input())
            if status == 'correto' :
                etapas_feitas += 1
                total_correto += 1
                print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
                print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {total_correto} ; Tentativas falhas - {total_falhas}')
                total_gasto_etapa += custo_etapa
                break
            elif status == 'incorreto' :
                etapas_feitas += 1
                total_falhas += 1
                print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}')
                total_gasto_etapa += custo_etapa
        else :
            print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {total_correto} ; Tentativas falhas - {total_falhas}')
    custo_etapa = 0
    etapas_feitas = 0
else :
    if nome_etapa == 'concluir' or nome_etapa == 'desistir' :
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')

if nome_etapa == 'concluir' :
    print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${total_gasto_etapa}')
elif nome_etapa == 'desistir' :
    print(f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${total_gasto_etapa}')
