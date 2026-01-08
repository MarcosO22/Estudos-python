soma = 0
con = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2== 0:
        soma +=n
        con+= 1
print('Você informou {} números PARES e a soma foi {}'.format(con,soma))