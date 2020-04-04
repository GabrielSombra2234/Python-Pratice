#bibliotéca#
from time import sleep

#decoração#
print('=' * 20)
sleep(0.7)
print(' 10 TERMOS DE UM PA ')
sleep(0.7)
print('=' * 20)
sleep(0.7)

#variaveis#
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a rasão: '))
decimo = primeiro + (10 - 1) * razao

#for#
for PA in range(primeiro, decimo + razao, razao):
    print(PA, end=' ')
print('Essa é a progreção dessa PA !')
