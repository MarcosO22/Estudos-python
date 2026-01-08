print('-='*20)
print("\033[4;30;45mAnalisador de Triângulos\033[m")
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('\033[4;30;47mOs segmentos acima PODEM FORMAR triângulos!\033[m')
else:
    print('\033[4;30;47mOs segmentos acima NÃO PODEM FORMAR triângulos!\033[m')