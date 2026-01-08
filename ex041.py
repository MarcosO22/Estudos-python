from datetime import date
an = int(input('Ano de nascimento: '))
atual = date.today().year
div = atual - an
if div <= 9:
    print('O atleta tem {} anos'.format(div))
    print('Classificado: \033[032mMIRIM\033[m')
elif div > 9 and div <= 14:
    print('O atleta tem {} anos'.format(div))
    print('Classificado: \033[032mINFANTIL\033[m ')
elif div > 14 and div <=19:
    print('O atleta tem {} anos '.format(div))
    print('Classificado: \033[032mJUNIOR\033[m')
elif div >19 and div <= 25:
    print('O atleta tem {} anos'.format(div))
    print('Classificado: \033[032mSêNIOR\033[m')
elif div > 25:
    print('O atleta tem {} anos '.format(div))
    print('Classificado: \033[032mMASTER\033[m')
