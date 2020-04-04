#váriaveis#
maior_idade = 0
media_total = 0
media_idade = 0
menor_idade = 0
nome_velho = ''

#estrutura_for#
for pessoa in range(1, 5):
    nome = str(input('Nome da {}° pessoa: '.format(pessoa))).upper().strip()
    sexo = str(input('Sexo da {}° pessoa [F/M]: '.format(pessoa))).strip().upper()
    idade = int(input('Idade da {}° pessoa: '.format(pessoa)))
    print('-' * 16)
#média_idade#
    media_idade += idade
    media_total = media_idade / 4

#homen_mais_velho#
    if pessoa == 1 and sexo == 'M':
        maior_idade = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

#mulher_menos_de_20#
    if sexo == 'F' and idade < 20:
        menor_idade += 1

#prints_respostas#
print('A média da idade do grupo é {} anos'.format(media_total))
print('O nome do homem mais velho é {}, com {} anos'.format(nome_velho, maior_idade))
print('Existem {} mulheres com menos de 20 anos'.format(menor_idade))
