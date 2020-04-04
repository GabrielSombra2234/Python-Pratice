vl = int(input('Qual o salário do funcionário ? R$ '))
if vl <= 1250:
    sli = vl + (vl * 15 / 100)
else:
    sli = vl + (vl * 10 / 100)
print('Seu salário de R$ {:.2f}, foi reajustado para R$ {:.2f}'.format(vl, sli))
