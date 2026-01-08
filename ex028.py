from random import randint
from time import sleep
print("-=-" *20)
print ('Tente advinhar em qual numero eu pensei de 1 á 10... ')
print('-=-' *20)
numero = int(input('Em qual número eu pensei? '))
cm = randint (1,10)
print('PROCESSANDO...')
sleep(3)
if cm == numero:
    print('Você acertou!! PARABÉNS')
else:
    print('Você andou perto! Eu pensei no número {} e não no {}'.format(cm, numero))