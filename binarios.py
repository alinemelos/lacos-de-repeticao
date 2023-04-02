# variaveis basicas
n_binario = str(input())
resposta = 0
contador = 0

# variaveis de controle
gabarito = False
chances = 3

while gabarito == False and chances > 0 :
    resposta = int(input())
    chances -= 1

    contador = int(n_binario, 2)

    if resposta == contador :
        gabarito = True
        chances = 0
    else :
        gabarito = False
        if chances > 0  :
            print(f'Resposta incorreta. Mas não desista! Você ainda tem {chances} chance(s).')
        elif chances == 0 :
            chances = 0
            gabarito = False
else:
    if gabarito == True :
        print('Parabéns!! Você acertou!')
        if resposta == 1:
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Porto de Galinhas (BRA).')
            print('Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')
        elif resposta == 2:
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Fernando de Noronha (BRA).')
            print('Belíssimas praias estão por vir.')
            print('Não esqueça o protetor solar.')
        elif resposta == 3:
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Gramado (BRA).')
            print('Aproveite passeios e paisagens espetaculares no sul do país!')
        elif resposta == 4:
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Berlim (ALE).')
            print('Desfrute de muita cultura e de experiências incríveis!')
            print('Prepare os casacos de frio!')
        elif resposta == 5:
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Tóquio (JPN).')
            print('Viva uma experiência inesquecível explorando um país do outro lado do mundo.')
            print('Prepare-se para muitas horas de voo!')
        else :
            print('Mas, infelizmente, hoje não é o seu dia de sorte.')
            print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
            print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
    elif gabarito == False :
        print('Infelizmente mais uma resposta incorreta.')
        print('Agradecemos sua participação!')
        if contador == 1 or contador == 2 or contador == 3 or contador == 4 or contador == 5 :
            print('Seu bilhete era premiado. Que pena!')
        else :
            print('Pelo menos seu bilhete não era premiado.')
            print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')