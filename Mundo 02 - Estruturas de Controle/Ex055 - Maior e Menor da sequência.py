#váriaveis_pesos#
maior_peso = 0
menor_peso = 0

#estrutura_for#
for peso in range(1, 6):
    peso_original = float(input('Digite o peso da {}° pessoa em Kg: '.format(peso)))

#estrutura_if#
    if peso == 1:
        maior_peso = peso_original
        menor_peso = peso_original
    else:
        if peso_original > maior_peso:
            maior_peso = peso_original
        if peso_original < menor_peso:
            menor_peso = peso_original
print('O maior peso lido foi {}Kg. \nE o menor peso lido foi {}Kg.'.format(maior_peso, menor_peso))
