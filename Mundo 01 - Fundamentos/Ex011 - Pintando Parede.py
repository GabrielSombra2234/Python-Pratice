larg = float(input('Qual a largura da parede< '))
alt = float(input('Qual a altura da parede< '))
área = larg * alt
tinta = área / 2
print('A dimenção da sua parede é de {} x {} e sua área e de {}m².'.format(larg, alt, área))
print('Para pintar a parede toda você precisa de {}l de tinta.'.format(tinta))
