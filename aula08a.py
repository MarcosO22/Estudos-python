import random
paises = ('brasil', 'grecia', 'alemanha', 'argentina')
paises_lisa = list(paises)
random.shuffle(paises_lisa)
print(f'Essa sera a ordem que voce irá viajar entre esses país: {paises_lisa}')