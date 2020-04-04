numero_primo = int(input('Digite um Numero: '))
total_de_vezes = 0
for verificador in range(1, numero_primo + 1):
    if numero_primo % verificador == 0:
        print('\033[33m', end=' ')
        total_de_vezes += 1
    else:
        print('\033[31m', end=' ')
    print(verificador, end=' ')
print('\n\033[m0 número {} foi divisível {} vezes'.format(numero_primo, total_de_vezes))
if total_de_vezes == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E pro isso ele não é PRIMO!')
