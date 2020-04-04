# froms #
from random import randint
from time import sleep

# Decoration #
print('\033[1;36m=-' * 28)
sleep(1)
print('I think in one number, between 1 to 10, can you guess ?')
sleep(1)
print('=-' * 28)
sleep(1)

# Random Number #
numero_computador = randint(1, 10)
palpites = 1
print('\033[1;33mThinking...')
sleep(1)
print('\033[1;32mComplete.')
sleep(1)

# while #
numero_jogador = int(input('\033[0;35mwhat number do you think it is: '))

sleep(1)
while not numero_jogador == numero_computador:
    palpites += 1
    if numero_jogador == numero_computador:
        print("You're right !!")
        print('Congratunations !!')
    else:
        print('No !, You missed !...')
        numero_jogador = int(input('Try again !: '))
        if numero_jogador != numero_computador and numero_jogador > numero_computador:
            print('\033[0;34mWrong !, lower..., try again.')
        elif numero_jogador != numero_computador and numero_jogador < numero_computador:
            print('\033[0;32mWrong !, higher..., try again.')
        elif numero_jogador == numero_computador:
            print("Now, you're right !! ")
print('\033[0;30mYou got it right with {} attempts, congratulations !!'.format(palpites))
