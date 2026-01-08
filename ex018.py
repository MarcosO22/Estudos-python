import math
from math import floor

grau = int(input('Digite o ângulo que você deseja: '))
angulo_radianos = math.radians(grau)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print('O angulo de {} tem o SENO de {:.2f} '.format(grau, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'. format(grau,cosseno))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(grau, tangente))