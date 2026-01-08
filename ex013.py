sala = float(input('Qual é o salário do Funcionário? R$'))
porc = sala + (sala*15/100)
print('Um funcionário que ganhava {}, com 15% aumento, passa a receber {:.2f}.'.format(sala,porc))