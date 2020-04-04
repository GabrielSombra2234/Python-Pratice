# froms #
from time import sleep

# decoração #
print('Operadores Númericos')
sleep(1)
print('''Menu [números de ordem]:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Comparação númerica
[ 4 ] Solicitar novos números
[ 5 ] Mostrar o menu novamente
[ 6 ] Sair do programa''')
sleep(1)

# ints #
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_or = int(input('Digite o número, correspondente ao que deseja fazer, por favor: '))

# while #
while not numero_or == 6:
# soma #
    if numero_or == 1:
        print('Somando...')
        sleep(1)
        resultado_1 = numero_1 + numero_2
        print('A soma entre [{}] e [{}], resulta em [{}].'.format(numero_1, numero_2, resultado_1))
        sleep(1)
        numero_or = int(input('O que você deseja fazer agora ?: '))
# multiplicão #
    elif numero_or == 2:
        print('Multiplicando...')
        sleep(1)
        resultado_2 = numero_1 * numero_2
        print('A multiplicação entre [{}] e [{}], resulta em [{}].'.format(numero_1, numero_2, resultado_2))
        sleep(1)
        numero_or = int(input('O que você deseja fazer agora ?: '))
# comparação #
    elif numero_or == 3:
        print('Comparando...')
        sleep(1)
    # maior #
        if numero_1 > numero_2:
            print('Entre os números [{}] e [{}], o maior entre os dois é [{}]'.format(numero_1, numero_2, numero_1))
            sleep(1)
    # menor #
        else:
            print('Entre os números [{}] e [{}], o maior entre os dois é [{}]'.format(numero_1, numero_2, numero_2))
            sleep(1)
        numero_or = int(input('O que você deseja fazer agora ?: '))
# novos numeros #
    elif numero_or == 4:
        print('Apagando...')
        sleep(1)
        numero_1 = int(input('Por favor, digite o novo primeiro número: '))
        sleep(1)
        numero_2 = int(input('Por favor, digite o novo segundo numero: '))
        sleep(1)
        numero_or = int(input('O que você deseja fazer agora ?: '))
        sleep(1)
# novo menu #
    elif numero_or == 5:
        print('Escrevendo...')
        sleep(1)
        print('''Menu [números de ordem]:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Comparação númerica
        [ 4 ] Solicitar novos números
        [ 5 ] Mostrar o menu novamente
        [ 6 ] Sair do programa''')
        sleep(1)
        numero_or = int(input('O que você deseja fazer desta vez: '))
        sleep(1)
# número invalido #
    else:
        print('Voçê não digitou nenhum [número de ordem] válido !, digite novamente !')
        sleep(1)
        print('''Menu [números de ordem]:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Comparação númerica
        [ 4 ] Solicitar novos números
        [ 5 ] Mostrar o menu novamente
        [ 6 ] Sair do programa''')
        sleep(1)
        numero_or = int(input('Digite o número, correspondente ao que deseja fazer, por favor: '))
print('-FIM-')
sleep(1)
