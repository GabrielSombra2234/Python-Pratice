#Bibliótecas#
from time import sleep

#Váriaveis#
acumulador = 0
contador = 0

#Somatório#
print('Números Multiplos de 3, Entre 1 a 500 e Sua Soma: ')
sleep(0.7)
for soma_dos_multiplos in range(1, 500+1, 2):
    if soma_dos_multiplos % 3 == 0:
        acumulador += soma_dos_multiplos
        contador += 1
print('O Valor dos {} Números Solicitados são {}'.format(contador, acumulador))
print('-FIM-')
