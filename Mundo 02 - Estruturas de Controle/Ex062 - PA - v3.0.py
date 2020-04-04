#bibliotecas#
from time import sleep

#decorações#
print('=' * 20)
sleep(0.7)
print(' GERADOR DE PA ')
sleep(0.7)
print('=' * 20)
sleep(0.7)

#variaveis#
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a rasão: '))
termo = primeiro_termo
cont = 1
total = 0
continuar = 10

#while#
while continuar != 0:
    total = total + continuar
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao #termo = termo + razao#
        cont += 1 #cont = cont + 1#
    print('PAUSA')
    continuar = int(input('Quantos termos você quer mostar mais ? '))
print('A Progreção foi finalizada com {} termos mostrados'.format(total))
print('\n-FIM-')
