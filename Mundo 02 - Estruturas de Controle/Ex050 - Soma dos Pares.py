#módulos#
from time import sleep

#Váriaveis#
acumulador = 0
contador = 0

#Informação#
print('-=' * 22)
sleep(0.4)
print('Contador de Numeros Pares')
sleep(0.4)
print('-=' * 22)
sleep(0.4)

#Estrutura For#
for numero_inteiro in range(1, 7):
    numero = int(input('Digite o {}° Numero: '.format(numero_inteiro)))
    if numero % 2 == 0:
        acumulador += numero
        contador += 1
print('Você digitou {} numeros, e sua soma é {}'.format(contador, acumulador))
print('Os numeros ímpares que foram digitados, foram desconciderados !!')
