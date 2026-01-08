from pydoc import resolve

preco = float(input('Qual e o preço do seu produto? R$ '))
desc = preco - (preco*5/100)
print('Você teve 5% de desconto. No total sua compra ficou {}'.format(desc))