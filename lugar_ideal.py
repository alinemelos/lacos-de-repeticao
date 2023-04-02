# variaveis gerais
qnt_lugar = int(input())
nome1 = ''
nome2 = ''
outro = ''
nota1 = 0
nota2 = 0
nota_outro = 0
pontos1 = 0
pontos2 = 0
pontos_outro = 0
melhor_lugar = ''
melhor_ponto = 0
pior_lugar = ''
pior_ponto = 0
lista = ''

# análise do lugar 1
nome1 = str(input())
while nota1 >= 0 :
    pontos1 += nota1
    nota1 = int(input())
# análise do lugar 2
nome2 = str(input())
while nota2 >= 0 :
    pontos2 += nota2
    nota2 = int(input())
# comparação dos 2 lugares
if pontos1 > pontos2 :
    melhor_lugar = nome1
    melhor_ponto = pontos1
    pior_lugar = nome2
    pior_ponto = pontos2
    lista = f'{nome1}'
elif pontos2 > pontos1 :
    melhor_lugar = nome2
    melhor_ponto = pontos2
    pior_lugar = nome1
    pior_ponto = pontos1
    lista = f'{nome2}'
elif pontos1 == pontos2 :
    melhor_lugar = nome1
    melhor_ponto = pontos1
    pior_lugar = nome1
    pior_ponto = pontos1
    lista = f'{nome1}, {nome2}'

#caso tiver mais de 2 lugares faz um loop com o for
for i in range(qnt_lugar - 2) :
    outro = str(input())
    # loop das notas
    while nota_outro >= 0 :
        pontos_outro += nota_outro
        nota_outro = int(input())
    #comparação do outro lugar com os iniciais
    if pontos_outro > melhor_ponto :
        melhor_lugar = outro
        melhor_ponto = pontos_outro
        lista = f'{outro}'
    elif pontos_outro < pior_ponto :
        pior_lugar = outro
        pior_ponto = pontos_outro
    elif pontos_outro == melhor_ponto :
        melhor_ponto = pontos_outro
        melhor_lugar = 'empate'
        lista += f', {outro}'
    nota_outro = 0
    pontos_outro = 0
    
# outputs
if melhor_lugar == 'empate' :
    print(lista)
    print('Tantas opções')
elif melhor_lugar != 'empate' :
    print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {melhor_ponto} vs {pior_ponto}')
