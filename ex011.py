larg = float(input('largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área e de {}m²'.format(larg,alt,area))
tinta = area / 2
print('Você precisará de {}l para pintar essa parede.'.format(tinta))