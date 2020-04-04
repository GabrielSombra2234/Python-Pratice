sálario = float(input('Qual o sálario do funcionario< R$'))
almento = sálario + (sálario * 15 / 100)
print('O sálario do funcionario era R${:.3f} e com 15% de almento ficou R${:.3f}'.format(sálario, almento))
