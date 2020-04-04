#módulos#
from datetime import date

#váriaveis#
maioridade = 0
menoridade = 0
contador = 0

#estrutura for#
for nascimento_1 in range(1, 8):
    nascimento_2 = int(input('\033[30m{}° Pessoa, digite seu ano de nascimento: '.format(nascimento_1)))

#calculo#
    contador += 1
    ano_atual = date.today().year
    idade_atual = ano_atual - nascimento_2
    print('\033[36m{} anos'.format(idade_atual))
#estrutura if#
    if idade_atual >= 18:
        maioridade += 1
    elif idade_atual <= 17:
        menoridade += 1
print('Foi digitado {} idade: \n\033[32m {} são maiores de idade \n\033[31m {} são menores de idade '.format(contador, maioridade, menoridade))
