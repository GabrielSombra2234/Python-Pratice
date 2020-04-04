vl = int(input('Qual a velocidade do carro em km/h: '))  # km/h
dv1 = vl - 80
dv2 = dv1 * 7  # R$
if vl > 80:
    print('Velocidade ultrapaçada, {} km/h, fua multa é de R$ {:.2f}.'.format(vl, dv2))
else:
    print('Você esta em velocidade correta, sem multas, PARABÉNS!')
