from itertools import count
nome = str(input('Qual é a frase? ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('Ela aparece primeiro na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))
