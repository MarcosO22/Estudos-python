ps = float(input('Qual é o seu peso? (kg) '))
al = float(input('Qual é a sua altura? (m)'))
imc = ps / (al ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Essa pessoa esta ABAIXO DO PESO!')
if imc >18.5 and imc <= 25:
    print('Essa pessoa esta no PESO IDEAL!')
if imc >25 and imc <= 30:
    print('Essa pessoa esta no SOBREPESO! CUIDADO!')
if imc> 30 and imc <= 40:
    print('Essa pessoa esta na OBESIDADE! CUIDE MAIS DE VOCÊ!')
if imc > 40:
    print("Essa pessoa esta com OBESIDADE MÓRBIDA! RISCO EMINENTE DE MORRER!")


