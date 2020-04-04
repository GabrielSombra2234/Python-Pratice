nu=int(input('Digite um número: '))
print('Dados do número...')
m=nu//1000%10
c=nu//100%10
d=nu//10%10
u=nu//1%10
print('milhar: {}'.format(m))
print('centena: {}'.format(c))
print('dezena: {}'.format(d))
print('unidade: {}'.format(u))
