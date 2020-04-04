a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('Organizando...')
# vendo quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# vendo quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))
