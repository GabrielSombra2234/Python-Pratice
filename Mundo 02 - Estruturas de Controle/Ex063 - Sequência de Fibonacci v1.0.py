#Bibliotécas#
from time import sleep

#prints#
print('-' * 45)
sleep(0.7)
print('Sequência de Fibonacci')
sleep(0.7)
print('-' * 45)
sleep(0.7)

#Variaveis#
fibonacci_1 = int(input('Quantos termos vocês quer mostrar ? '))
numero_1 = 0
numero_2 = 1
cont = 3

#Prints 2#
print('~' * 45)
print('{} → {}'.format(numero_1, numero_2), end='')

#while#
while cont <= fibonacci_1:
    numero_3 = numero_1 + numero_2
    print(' → {}'.format(numero_3),end='')
    cont += 1
    numero_1 = numero_2
    numero_2 = numero_3
print(' → FIM')
print('A sequência terminou com, {} termos mostrados!'.format(cont - 1))
print('~' * 45)
