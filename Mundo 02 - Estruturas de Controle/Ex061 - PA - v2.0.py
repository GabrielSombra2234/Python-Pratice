#bibliotecas#
from time import sleep

#decorações#
print('=' * 20)
sleep(0.7)
print(' 10 TERMOS DE UMA PA ')
sleep(0.7)
print('=' * 20)
sleep(0.7)

#variaveis#
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a rasão: '))
começo = primeiro_termo
cont = 1

#while#
while cont <= 10:
    print('{} -'.format(primeiro_termo), end='')
    primeiro_termo += razao #primeiro_termo = primeiro_termo + razao#
    cont += 1 #cont = cont + 1#
print('FIM')
