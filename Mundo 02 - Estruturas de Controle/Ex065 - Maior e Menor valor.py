#Bibliotécas#
from time import sleep

#Prints#
print('-' * 25)
print('Números Maiores')
print('-' * 25)

#Variáveis#
numero_menor = numero_maior = 0
numero_media = numero_resultado =  0
cont = 0
loop = 'S'

#While e If#
while loop == 'S':
    numero_cont = int(input('Digite um número: '))
    numero_resultado += numero_cont
    print('-' * 25)
    cont += 1
    if cont == 1:
        numero_maior = numero_menor = numero_cont
    else:
        if numero_cont > numero_maior:
            numero_maior = numero_cont
        elif numero_cont < numero_menor:
            numero_menor = numero_cont
    loop = str(input('Você deseja continuar, [S/N] ? ')).upper().strip()[0]

#Resultado#
numero_media = numero_resultado / cont
print('O programa terminou com {} números mostrados, e a média entre eles é {}.'.format(cont, numero_media))
print('O maior número mostrado é {}, e o menor número mostrado é {}.'.format(numero_maior, numero_menor))
print('FIM')
