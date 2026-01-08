nome = str (input('Qual e o seu nome? '))
if nome == 'Gusstavo':
    print("Que nome bonito gustavo!")
elif nome == 'Pedro' or nome == "Joao" or nome == 'paulo':
    print('Seu nome e bem popular no Brasil!')
elif nome == 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Que nome comum!')
print('Tenha um bom dia, {}'.format(nome))