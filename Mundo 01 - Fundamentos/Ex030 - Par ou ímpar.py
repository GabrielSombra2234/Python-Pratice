nm = int(input('Digite um número: '))
rt = nm % 2
print('Analizando seu número...')
if rt == 0:
    print('O número {} é PAR'.format(nm))
else:
    print('O número {} é ÍMPAR'.format(nm))
