# lacos-de-repeticao
codigos de aprendizado sobre laços de repeticao
<h3>Apostas</h3>
O jogo funciona da seguinte forma:

Uma pessoa X deverá dizer quantos dardos consegue acertar no alvo em 3 tentativas, a pessoa X deve apostar um valor em si mesma como forma de mostrar o quão confiante está de realizar determinada atividade. Enquanto isso, as outras três pessoas poderão ou não apostar contra, acreditando que a pessoa X não terá capacidade de realizar o desafio. Pelo menos 1 pessoa sempre vai apostar contra.

Regra 1: Se a pessoa X cumprir o desafio proposto, receberá a soma dos valores apostados contra ela e as pessoas que apostaram contra perderão do seu saldo o respectivo valor apostado.

Regra 2: Se a pessoa X não conseguir cumprir, deverá enviar um PIX no valor que apostou para cada pessoa que apostou contra e, obviamente, todo esse valor deve ser tirado do seu saldo.

Exemplo:

Misheldon disse que conseguiria acertar o alvo 3 vezes nas 3 tentativas e apostou R$100,00 nisso, mas ao final das tentativas ele só somou 2 acertos. Frej, Guga e Artur apostaram R$120 que Misheldon não seria capaz de conseguir cumprir o desafio, então Misheldon teve que pagar R$100 reais a cada um deles, ficando assim com -300 de saldo. Já Artur, Frej e Guga ficaram com R$100 de saldo cada.

Sua missão é construir um sistema para computar o saldo e, ao final das rodadas, printar o resultado final dos saldos.

Input

O input consiste em:

Quantidade de rodadas
E, para cada rodada:
Nome do jogador
Valor da aposta do jogador
Quantidade de acertos estimada
Quantidade de amigos que apostaram contra (K)
Nome de quem apostou contra (1)
Valor apostado (1)
…
Nome de quem apostou contra (K)
Valor de apostado (K)
Expressão pós jogada 1
...
Expressão pós jogada 3

Output

“Rodada numero {num_rodada}” → A cada rodada
“Jogador: {nome_jogador}” → após o segundo input
“Valor apostado: {valor_apostado}” → após o terceiro input
“Acreditando que acerta {qnt} vezes em 3 tentativas” → após a quantidade de acertos estimada
"{qnt_contra} amigos apostaram contra" → após a quantidade de amigos que apostaram contra
"Parece que {pessoa} está sendo subestimado!” → além do print de cima, é printado se a quantidade de pessoas que apostaram contra for == 3
“{nome_apostador} apostou {valor_aposta}" → após cada aposta declarada
“Errou! Restam {Y} tentativas” → se a expressão pós jogada for diferente de “Receba!”

Ao final de todas as rodadas, você deve printar os resultados:
Fim de jogo, o resultado foi:
Artur ficou com A1 de saldo
Frej ficou com F1 de saldo
Guga ficou com G1 de saldo
Misheldon ficou com M1 de saldo

sendo A1, F1, G1 e M1 o valor do saldo de cada respectivo jogador após o final das rodadas.

OBS: O saldo de todos os jogadores começa como 0 e pode ficar negativo.
<h3>Binario e palavras inversas </h3>
Filipe Calegário está aproveitando suas férias nos cassinos de Las Vegas, quando um homem o aborda propondo um jogo apostando dinheiro, ele o diz que esse jogo necessita apenas de habilidade para ganhar e que não há trapaças.
Calegário aceita jogar o jogo após as falas do apostador e a promessa de um jogo limpo.
As regras são:

O apostador irá falar uma palavra para o jogador fazer uma ação com ela. As ações podem ser:
1 - colocar a palavra de trás pra frente. EX.: palavra = carro / Resposta certa = orrac
2 - colocar a palavra em binário. EX.: palavra = aviao / resposta certa = 0110000101110110011010010110000101101111

Dica: pesquisar sobre tabela ASCII e comando ord()
OBS1: As respostas devem vir em string
OBS2: Proibido uso de bin() e de slicing

Cada um dos participantes tem 3 vidas, caso Calegário erre em uma rodada perderá 1 vida, caso ele acerte o apostador é quem terá 1 vida descontada.
Para garantir que não haja trapaça no jogo, Calegário convoca você para fazer um programa que corrija as respostas dele e conte as vidas corretamente.

Input

Você vai receber os inputs de cada rodada contendo a palavra da vez, o numero que representa a ação e a resposta de Calegário
palavra_1
acao_1
resposta_1
...

OBS.3: você receberá inputs enquanto ambos os jogadores ainda estiverem com vida.

Output
Após cada rodada, seu programa deve imprimir:
"Rodada Concluída!"
“{participante que perdeu} perdeu uma vida”

Caso Calegário acerte uma conversão de palavra para binário:
“Como alguém consegue fazer isso de cabeça?”

Quando algum dos dois chegar a zero de vida, seu código deve imprimir:
“Partida Concluída!”
“Vencedor: {vencedor}”

Caso o apostador tenha ganho:
“HAHAHA, acha mesmo que preciso trapacear para ganhar de você?”

Caso Calegario tenha ganho:
"Droga, não acredito que eu perdi essa partida, achei que seria uma vitória fácil..."
<h3>Binarios</h3>
desenvolver um programa que, ao receber o número sorteado e o palpite inicial do cliente, converta o número binário para decimal através de laços de repetição e verifique se o cliente acertou. O cliente possui até 03 chances para acertar, mas atenção: O cliente só irá falar um próximo palpite se realmente tiver errado o anterior.
Caso o palpite esteja correto, o programa deverá verificar qual será o destino premiado de acordo com a tabela abaixo, que foi divulgada pela a empresa:
<img src="https://i.postimg.cc/Rhbv7Bqr/Cin-Tour-2.png">
Atenção: A empresa também colocou no sorteio números inválidos, ou seja, que não correspondem a nenhum destino.

OBS.1: Sendo a entrada um valor em binário, trabalhe no formato de string.
OBS.2 : Todas as entradas serão amigáveis (Não precisa se preocupar com números negativos).

Input

Inicialmente, você receberá o número sorteado (em binário):
n_binario

Em seguida, será fornecido o primeiro palpite do cliente (em decimal):
palpite_01
Se, e somente se, o cliente errar, mais um palpite será recebido (também em decimal):
palpite_02
Se, e somente se, o cliente errar novamente, mais um palpite será recebido (também em decimal):
palpite_03

Output

Caso o cliente tenha acertado, imprima:
“Parabéns!! Você acertou!”
Em seguida, observe se era ou não um bilhete premiado e imprima:

Caso o destino seja Porto de Galinhas:

“Férias inesquecíveis estão te esperando!"
"Seu destino será Porto de Galinhas (BRA)."
"Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!”

Caso o destino seja Fernando de Noronha:

“Férias inesquecíveis estão te esperando!"
"Seu destino será Fernando de Noronha (BRA)."
"Belíssimas praias estão por vir."
"Não esqueça o protetor solar.”

Caso o destino seja Gramado:

“Férias inesquecíveis estão te esperando!"
"Seu destino será Gramado (BRA)."
"Aproveite passeios e paisagens espetaculares no sul do país!”

Caso o destino seja Berlim:

“Férias inesquecíveis estão te esperando!"
"Seu destino será Berlim (ALE)."
"Desfrute de muita cultura e de experiências incríveis!"
"Prepare os casacos de frio!”

Caso o destino seja Tóquio:

“Férias inesquecíveis estão te esperando!"
"Seu destino será Tóquio (JPN)."
"Viva uma experiência inesquecível explorando um país do outro lado do mundo."
"Prepare-se para muitas horas de voo!”

Caso o número não corresponda a nenhum destino:
“Mas, infelizmente, hoje não é o seu dia de sorte."
"Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio."
"Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!”

Porém, caso o cliente tenha informado a resposta incorreta, imprima:
Se ele ainda possui chance(s) para adivinhar:
“Resposta incorreta. Mas não desista! Você ainda tem { n_chances } chance(s).”
e repita o processo.

Ou se errou em todas as suas tentativas:

Caso o bilhete correspondesse a um destino:
“Infelizmente mais uma resposta incorreta."
"Agradecemos sua participação!"
"Seu bilhete era premiado. Que pena!”

Ou caso o bilhete não correspondesse a um destino:
“Infelizmente mais uma resposta incorreta."
"Agradecemos sua participação!"
"Pelo menos seu bilhete não era premiado."
"Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!”
<h3>Construcao</h3>
Input

Inicialmente, você receberá o nome da invenção:

nome_invencao

Em seguida, serão fornecidas n vezes as informações acerca de cada etapa:

nome_etapa

custo_etapa

tentativas_etapa

OBS.1: Há casos em que nem todas as entradas sobre a etapa serão necessárias; nessas situações, elas não serão fornecidas. As etapas "concluir" e "desistir" não possuem custo nem tentativas, a entrada "dar um plus" possui custo mas não tentativas, todas outras etapas possuem custo E tentantivas

OBS.2: Para uma mesma etapa, todas as tentativas têm o mesmo custo.

Para cada tentativa, você receberá uma entrada que indicará o status dessa etapa, o qual será "correto" ou "incorreto":

status_etapa

OBS.3: No máximo um dos status será "correto". Após recebê-lo, você não deverá continuar realizando as tentativas restantes.

Output

Enquanto você recebe as entradas das etapas, você deve imprimir:

Caso a etapa seja "desistir" ou "concluir":
"A jornada da construção do(a) {invencao} acaba aqui."

Nesse caso, não serão fornecidas as entrada de custo nem de tentativas e deve-se interromper a chamada de novas etapas.

Caso a entrada seja "dar um plus":
"Agora o(a) {invencao} ficou ainda mais legal! Pena que precisei gastar R${custo}"

Nesse caso, será fornecida apenas a entrada de custo, a entrada de tentativas não será fornecida.

Ambos os casos citados acima não serão contabilizados no andamento do projeto como etapas realizadas.

Para os outros casos, você imprimirá:

Se o status for "incorreto" :
"Ainda não consegui {etapa} corretamente, e essa tentativa me custou R${custo}"

Se o status for "correto":
"Oba! consegui {etapa}, o que me custou R${custo}"

Em que, {custo} é um valor inteiro referente à realização daquela única etapa.

Após realizar todas as tentativas necessárias de cada etapa, você deve imprimir:

"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_REALIZADAS} ; Tentativas falhas - {total_falhas}"

Por fim, você deve imprimir:

Se você desistiu:
"Infelizmente, o sonho do(a) {invencao} foi interrompido e levou junto com ele R${despesa_total}"

Se você concluiu:
"Uhuuu, finalmente o(a) {invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}"
<h3>Lugar ideal</h3>
Input

A primeira entrada é um inteiro N ≥ 2 que representa o total de lugares que serão sugeridos.

N

Em seguida, o programa receberá uma string contendo o nome do lugar sugerido.

nome_lugar

A sugestão então receberá um número indefinido de notas, parando quando uma das notas tiver um valor menor que 0 (o valor negativo não deve contar para o total de pontos que uma sugestão recebeu).

nota1

nota2

nota3

…

nota < 0

Esse processo se repetirá N vezes.

Output

Se não ocorrer empate para o melhor_lugar
{melhor_lugar} ganhou de lavada de {pior_lugar}, com {maior_nota} vs {pior_nota}

Se ocorrer empate para melhor_lugar
{melhor_lugar1}, {melhor_lugar2}, (…) , {melhor_lugarN}

Tantas opções

OBS: Não existem casos onde seja preciso imprimir mais que um pior_lugar

OBS2: Em caso de empate, os lugares vão ser mostrados separados por vírgula e em ordem de entrada. Lembrem-se que vocês ainda não podem usar listas, pensem em uma outra maneira de armazenar a informação dos melhores lugares
<h3>Praia</h3>
É verão e você quer curtir um dia nas belíssimas praias de Maragogi, o Caribe brasileiro. Você acabou de tomar seu café da manhã, e quer se preparar para tomar o tão esperado banho de mar. Para ter o dia perfeito de praia, você deve passar seu filtro solar e separar um dinheiro para tomar aquela água de coco de lei. Se estiver chovendo, você não poderá ir à praia.

No início do dia, você se encontra:

Sem protetor solar

0 reais na carteira

Clima ensolarado

Input

Você receberá inúmeras entradas contendo ações realizadas por você ou uma mudança do clima, até receber a entrada “ir para a praia”. As ações podem ser as seguintes:

separar dinheiro → Pede uma nova entrada, em float, que representa a quantia adicionada à carteira

passar protetor → Passa o protetor ¯_(ツ)_/¯

choveu → Muda o clima para "chuvoso"

parou de chover → Muda o clima para "ensolarado"

ir para a praia → Finaliza os acontecimentos

Obs.: Caso apareça uma entrada diferente dessas ações, seu programa deverá ignorar.

Output

Você deve se preparar para dois tipos de saídas: uma para se você vai à praia ou não, e outra para como você chegou da praia.

Se o clima estiver chuvoso:

Hoje não vai dar pra ir, chuvinha barrou

Se o clima estiver ensolarado:

Hoje tem sol e mar!

A segunda mensagem só será realizada se você foi à praia:

Se você não passou protetor e está com menos de 10 reais:

Você não chegou muito bem, chame um médico!

Se você não passou protetor e está com 10 ou mais reais:

O novo camarão do CIn foi criado

Se você passou protetor e está com menos de 10 reais:

Só faltou uma aguinha de coco...

Se você passou protetor e está com 10 ou mais reais:

Aí sim! Hoje rendeu!
<h3>Sequências</h3>
Input

A entrada se comportará da seguinte forma:

N

N é a quantidade de jogos em promoção

nome1

numero_sequencia1

nome2

numero_sequencia2

...

nomeN

numero_sequenciaN

quantidade N de strings, que são os nomes dos jogos em promoção.

Output

Para cada jogo na lista:

Se você achar uma sequência não direta (ex: KingdomHearts 5, ao invés do 2), imprima:

“Achamos {nome_jogo_promocao}, mas você ainda precisa jogar o 2, 3, …, (N-1) antes desse.”

Se você achar a sequência direta, ou seja, o jogo for o 2, imprima:

“Achei a sequel! Hora da diversão!”
<h3>Viagens</h3>
O jogo funcionará assim:

1 - Eles irão usar um programa aleatório que irá sortear uma letra.

2 - Eles deverão usar o nome dos seus estados para comparação.

3 - Ganha qual nome do estado tiver mais repetições da letra sorteada.

por exemplo:

letra sorteada: a

estado do amigo1: Pernambuco

estado do amigo2: Maranhão

O amigo2 ganha pois Maranhão possui 3 letras ‘a’ e Pernambuco apenas 1.

A quantidade de dias que Victor irá ficar naquele estado com seu amigo é igual a quantidade de vezes que a letra aparecer. Além disso, ele também irá definir por qual estado prefere começar a viagem.

OBS:: Não é permitido o uso da função count().

Input

A entrada seguirá o modelo abaixo:

letra_sorteada

quantidade_de_amigos

estado_de_preferencia

nome_amigo_1

estado_1

. . .

nome_amigo_N

estado_N

Sendo N a quantidade de amigos.

Lembrando que as entradas são amigáveis.

Output

Se o estado de preferencia for o ganhador, deverá aparecer a seguinte mensagem:

"UHUL!!! Victor vai começar por X que é o estado que ele queria e ficara la por Y dias."

Se for outro estado, deverá aparecer essa mensagem:

"Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado X e ficara la por Y dias."

LEMBRANDO QUE NÃO HAVERÁ EMPATES E SEMPRE TERÁ O ESTADO GANHADOR.
