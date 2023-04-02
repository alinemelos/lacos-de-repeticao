qnt_jogos = int(input())
quantia = 0
nome = ''
sequel = 0
var = ''

while qnt_jogos > 0 :
    nome = str(input())
    sequel = int(input())
    qnt_jogos -= 1
    if sequel > 2 :
      var = ''
      for i in range(2,sequel,1):
        if i >= 2 :
          if i < sequel - 1 :
            var += str(i) + ', '
          elif i == sequel - 1 :
            var += str(i)
        elif i != 2 :
          var += str(i)
      print(f'Achamos {nome} {sequel}, mas você ainda precisa jogar o {var} antes desse.')
    elif sequel == 2 :
        print('Achei a sequel! Hora da diversão!')
else :
    quantia = 0