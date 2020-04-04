#Módulos#
from time import sleep

#Decoração#
print('=-' * 18)
sleep(1)
print('Tabuada Digital')
sleep(1)
print('=-' * 18)
sleep(1)

#Estrutura For#
multiplicando = int(input('Diga Um Número: '))
for multiplicador in range(1, 10+1):
    resuldado = multiplicando * multiplicador
    print('O Número {} X {} = {}'.format(multiplicando, multiplicador, resuldado))
    sleep(1)
print('--Fim--')
sleep(1)

#O Número {} multiplicado por {}, é igual a {}#
