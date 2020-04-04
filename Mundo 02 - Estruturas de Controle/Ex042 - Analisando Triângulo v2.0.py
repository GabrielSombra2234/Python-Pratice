#Apresentation:

print('\033[1;36m-=' * 20)
print('Analizador de Triângulos')
print('-=' * 20)

#Input Information:

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

#Data Analize:

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Esses Segmentos, Podem Formar Um Triâmgulo: ', end='')
   if r1 == r2 == r3:
       print('EQUILÁTERO')
   elif r1 != r2 != r3 != r1:
        print('ESCALENO')
   else:
    print('ISÓCELES')
else:
    print('Esses Segmentos Não Podem Formar Um Triângulo')
