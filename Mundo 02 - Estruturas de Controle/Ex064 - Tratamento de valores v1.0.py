#Bibliotécas#
from time import sleep

#Prints#
print('-' * 25)
sleep(0.7)
print('Condição de parada')
sleep(0.7)
print('-' * 25)
sleep(0.7)
print("[Digite 999 para sair]")
sleep(0.7)

#Variáveis#
cont = numero_soma = resultado = 0
numero_soma = int(input('Digite um número: '))
print('-' * 25)
#while#
while numero_soma != 999:
        resultado += numero_soma
        cont += 1
        numero_soma = int(input('Digite um número: '))
        print('-' * 25)

#Prints fim#
print('O programa terminou com {} números mostrados.'.format(cont))
sleep(0.7)
print('E a soma entre esses números resulta em {}.'.format(resultado))
sleep(0.7)
print('FIM')
