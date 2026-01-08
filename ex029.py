carro = float(input('Qual a velocidade atual do carro? '))
if  carro > 80:
    multa = (carro - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. \nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

