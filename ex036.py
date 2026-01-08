casa = float(input('Qual o valor da casa? '))
sala = float(input('Qual o seu sálario? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
vez = casa / (anos * 12)
minimo = sala * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa,anos), end='')
print('O valor da parcela fica R${:.2f}'.format(vez))
if vez <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo NEGADO!')

