#Jogo: Pedra, Papel, Tesoura

#Bibliotécas:
from random import randint
from time import sleep

#Apresentação:
print('Jogo Pedra, Papel, Tesoura !')
sleep(1)
print('Contra a Maquina !')
sleep(0.5)
print('Números Equivalentes:')
print('[ 0 ] Pedra')
sleep(0.5)
print('[ 1 ] Papel')
sleep(0.5)
print('[ 2 ] Tesoura')
sleep(0.5)

#Sorte:
numero_aleatorio = randint(0, 2)
numero_da_Sorte = int(input('Qual Número Será ? '))
sleep(0.5)

#Caminhos:
if numero_aleatorio == 0 and numero_da_Sorte == 1 or numero_da_Sorte == 0 or numero_da_Sorte == 2:
    print('Número Escolhido pela Maquina foi {} !!'.format(numero_aleatorio))
    print('Número Escolhido pelo Jogador foi {} !!'.format(numero_da_Sorte))
    print('''Regra do Jogo:
    0 Contra 0 = Empate !
    0 Contra 1 = Vitória !
    0 Contra 2 = Derrota !
    Boa Sorte !!!''')

elif numero_aleatorio == 1 and numero_da_Sorte == 1 or numero_da_Sorte == 0 or numero_da_Sorte == 2:
    print('Número Escolhido pela Maquina foi {} !!'.format(numero_aleatorio))
    print('Número Escolhido pelo Jogador foi {} !!'.format(numero_da_Sorte))
    print('''Regra do Jogo:
    1 Contra 0 = Vitoria !
    1 Contra 1 = Empate !
    1 Contra 2 = Derrota !
    Boa Sorte !!!''')

elif numero_aleatorio == 2 and numero_da_Sorte == 1 or numero_da_Sorte == 0 or numero_da_Sorte == 2:
    print('Número Escolhido pela Maquina foi {} !!'.format(numero_aleatorio))
    print('Número Escolhido pelo Jogador foi {} !!'.format(numero_da_Sorte))
    print('''Regra do Jogo:
    2 Contra 0 = Derrota !
    2 Contra 1 = Vitória !
    2 Contra 2 = Empate !
    Boa Sorte !!!''')

elif numero_da_Sorte > 2:
    print('Número Inválido, Digite os Números Conforme a Tabela !!!')