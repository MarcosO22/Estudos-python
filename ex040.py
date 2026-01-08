num = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
sm = (num + n2)/2
if sm <5:
    print('Tirando {} e {}, a média do aluno é {}'.format(num,n2,sm))
    print('O aluno está REPROVADO')
elif sm >5:
    print('Tirando {} e {}, a média do aluno é {}'.format(num, n2,sm))
    print('O aluno está APROVADO')