# from #
from random import randint
from time import sleep

# Decoração #
print('-=-' * 20)
sleep(1)
print('Vou pensar em um número de 0 a 5, Tente adivinhar...')
sleep(1)
print('-=-' * 20)
sleep(1)

# Programa #
jgd = int(input('Em que número eu pensei ? ')) # Usuário tenta acertar #
cpt = randint(0, 10)  # Faz o computador gerar um número  #
print('PROCESSANDO...')
sleep(1)

# IFs #
if jgd == cpt:
    print('PARABÊNS, Você ganhou!')
    print('O número pensado foi {}'.format(cpt))
else:
    print('Que pena, A MAQUINA VENCEU!')
    print('O número pensado foi {}.'.format(cpt))
