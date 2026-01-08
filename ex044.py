print('='*12,'LOJAS GUANABARA','='*12)
pr = float(input('Preços das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Sua escolha:'))
if opção ==1:
    total = pr - (pr * 10 / 100)
elif opção ==2:
    total = pr - (pr * 5 / 100)
elif opção == 3:
    total = pr / 2
elif opção == 4:
    total = pr + (pr * 20 / 100)
    totparce = int(input('Quantas parcelas?'))
    parcela = total / totparce
    print('Sua compra será parcelada em {}x de R${} COM JUROS '.format(totparce,parcela))
else:
    total = pr
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pr, total))
