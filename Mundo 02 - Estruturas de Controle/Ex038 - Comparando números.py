print('-=' * 14)
print('Qual é o maior.')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('=-' * 14)
if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que {}.'.format(num2, num1))
else:
    print('Não exite diferença, {} e {} são iguais'.format(num1, num2))
