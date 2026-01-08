hj = int(input('Digite um número inteiro: '))
print('''Escolha uma das basses das conversão:  
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(hj,bin(hj)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(hj,oct(hj)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(hj,hex(hj)[2:]))
else:
    print('Opção inválida! Tente novamente!')