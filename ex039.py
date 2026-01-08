from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
ida = atual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc,ida,atual))
if ida ==18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif ida <18:
    saldo = atual - nasc
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif ida >18:
    saldo = ida - 18
    print('Você deveria ter se alistado em {} anos'.format(saldo))
    ano = atual- saldo
    print("Seu alistamento foi em {}".format(ano))