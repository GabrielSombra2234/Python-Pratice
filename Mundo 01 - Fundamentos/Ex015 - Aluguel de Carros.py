dias = int(input('Quantos dias foram alugados< '))
km = float(input('Quantos km rodados< '))
preço = (dias * 60) + (km * 0.15)
print('O preço total a pagar é {:.2f}'.format(preço))
