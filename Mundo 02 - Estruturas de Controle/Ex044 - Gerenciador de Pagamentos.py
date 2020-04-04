#Price:

print(f'{" ZainTech ":=^40}')
print('"Qual Tecnologia você vai comprar hoje?"')
valor_original = float(input('Qual o valor do Produto CA$ '))

#Payment Methods:

print(''' FORMAS DE PAGAMENT0
[ 1 ] A vista no Dinheiro/Cheque (20% DE DESCONTO)
[ 2 ] A vista no Cartão de Débito/Crédito (10% DE DESCONTO)
[ 3 ] 2x no Cartão de Cédito (PREÇO NORMAL)
[ 4 ] 3x ou mais no Cartão de Crédito (COM 20% DE JUROS)''')
forma_de_pagamento = int(input('Qual a forma de pagamento: '))

#Desconts and Interest:
if forma_de_pagamento == 1:
    valor_novo = valor_original * 0.2
    valor_novo_2 = valor_original - valor_novo
    print('Valor Original: CA${:.2f}'.format(valor_original))
    print('Valor Novo ou Total a Pagar: CA${:.2f}'.format(valor_novo_2))

elif forma_de_pagamento == 2:
    valor_novo = valor_original * 0.1
    valor_novo_2 = valor_original - valor_novo
    print('Valor Original: CA${:.2f}'.format(valor_original))
    print('Valor Novo ou Total a Pagar: CA${:.2f}'.format(valor_novo_2))

elif forma_de_pagamento == 3:
    valor_dividido = valor_original / 2
    print('Valor Original: CA${:.2f}'.format(valor_original))
    print('Valor Novo ou Total a Pagar: CA${:.2f}'.format(valor_original))
    print('Valor Parcelado em 2x de R${:.2f}, Ficara CA${:.2f} por Mês.'.format(valor_original, valor_dividido))

elif forma_de_pagamento == 4:
    quantidade_de_parcelas = int(input('Quantas Parcelas Serão ?: '))
    valor_novo = valor_original * 0.2
    valor_novo_2 = valor_original + valor_novo
    valor_de_divisao = valor_novo_2 / quantidade_de_parcelas
    print('Valor Original: CA${:.2f}'.format(valor_original))
    print('Valor Novo ou Total a Pagar: CA${:.2f}'.format(valor_novo_2))
    print('Valor Parcelado em {}x de CA${:.2f}, Ficara CA${:.2f} por Mês.'.format(quantidade_de_parcelas, valor_novo_2, valor_de_divisao))

else:
    print('Forma de Pagamento Inexistente, Escolha os Outros Números Acima!!! Arigato!!! ')
