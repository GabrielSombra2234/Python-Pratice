preço = float(input('Qual o preço do produto< R$'))
novo = preço - (preço * 5 / 100)
print('O preço do produto é R${:.2f} reais e com 5% de desconto fica R${:.2f} reais.'.format(preço, novo))
