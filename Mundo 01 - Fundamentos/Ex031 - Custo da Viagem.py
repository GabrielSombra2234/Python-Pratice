dts = float(input('Quantos km têm a sua viagêm ? '))
print('PARABÊNS!, você está prestes a fazer uma viagêm de {}Km/h'.format(dts))
if dts <= 200:
    prc = dts * 0.50
else:
    prc = dts * 0.45
print('O preço de uma viagêm de {}Km é de R${:.2f}'.format(dts, prc))

'''dsc=float(input('Qual a distância da sua viagem em km: '))
km1=dsc*0.50
km2=dsc*0.45
print('Cáculando...')
if dsc>=200:
    print('O total a pagar é R$ {:.2f} por km.'.format(km2))
else:
    print('O total a pagar é R$ {:.2f} por km.'.format(km1))'''
# O de cima, fui eu que criei
