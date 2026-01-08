num = int(input('Primeiro número: '))
se = int(input('Segundo número: '))
if num< se:
    print('O SEGUNDO valor é maior')
elif se>num:
    print('\033[033mO PRIMEIRO valor é maior\033[m ')

else:
    print('Os dois valores são IGUAIS')
