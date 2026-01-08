

passa = int(input('Qual e a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(passa))
if passa <= 200:
    preco = passa * 0.50

else:
    preco = passa * 0.45
print('E o preço da sua passagem será de R${:.2F}.'.format(preco))


