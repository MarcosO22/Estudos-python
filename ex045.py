from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opc = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
computador = randint (0,2)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[opc]))
if computador == 0:
    if opc== 0:
        print('EMPATE')
    elif opc == 1:
        print('JOGADOR VENCE')
    elif opc ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador ==1:
    if opc == 0:
        print('COMPUTADOR VENCE')
    elif opc ==1:
        print('EMPATE')

    elif opc ==2:
        print('jogador vence')
    else:
        print('JOGADA INVÁLIDA')
elif computador== 2:
    if opc ==0:
        print('JOGADOR VENCE')
elif opc==1:
    print('COMPUTADOR VENCE')
elif opc== 2:
    print('EMPATE')
else:
    print('JOGADA INVALIDA')


