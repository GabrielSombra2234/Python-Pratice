from math import factorial

numero = int(input('Digite um número, para saber o seu fatorial !: '))
fator = factorial(numero)
print('o fatorial de {}!, é {:.1f}.'.format(numero, fator))
