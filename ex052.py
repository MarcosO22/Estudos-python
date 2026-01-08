i = int(input('Digite um numero: '))
tot = 0
for c in range(1, i +1):
    if i % c ==0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[031m', end='')
    print('{} '.format(c), end ='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(i, tot))
if tot ==2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')