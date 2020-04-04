from datetime import date

# Nome
print('\033[0;36mOlá, Bom dia Nadador!')
idd = int(input('Qual seu ano de nascimento: '))
idd2 = date.today().year
idd3 = idd2 - idd
print('Você tem {} anos de idade'.format(idd3))

# If
if idd3 <= 9:
    print('Classificação: MIRIM!; Que no Qual, Vai Até 9 Anos de Idade!')
elif idd3 <= 14:
    print('Classificação: INFANTIL!; Que no Qual, Vai Até 14 Anos de Idade!')
elif idd3 <= 19:
    print('Classificação: JUNIOR!; Que no Qual, Vai Até 19 Anos de Idade!')
elif idd3 <= 24:
    print('Classificação: SÊNIOR!; Que no Qual, Vai Até 24 Anos de Idade!')
else:
    print('Classificação: MASTER!; Que no Qual, é Acima De 25 Anos de Idade!')
