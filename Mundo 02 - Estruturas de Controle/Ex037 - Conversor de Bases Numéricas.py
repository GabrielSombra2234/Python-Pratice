num = int(input('\033[1;31mDigite um número: '))
print('-=' * 16)
print('''Escolha uma base de converção
[1] Binário
[2] Octadecimal
[3] Hexadecimal''')
num2 = int(input('\033[1;31mDigite a sua escolha: '))
print('-=' * 16)
if num2 == 1:
    print('\033[1;32mO número {} é igual a {} em Binário.'.format(num, bin(num)[2:]))
elif num2 == 2:
    print('\033[1;36mO número {} é igual a {} em Octadecimal.'.format(num, oct(num)[2:]))
elif num2 == 3:
    print('\033[1;32mO número {} é igual a {} em Hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Opção incorreta, Tente novamente.')
