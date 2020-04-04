nm1=str(input('Qual seu nome completo ?: ')).strip().title()
nm2=nm1.split()
print('{}, Têm Silva nesse nome, {}.'.format(nm1,'Silva'in nm2))
