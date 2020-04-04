#Bibliotécas#
from time import sleep

#Perguntas Primárias#
print('\033[1;32mConsultoria de Emprestimo.')
v1 = float(input('\033[1;36mQual o valor da casa: R$'))
v2 = float(input('\033[1;36mQuanto é o seu sálario: R$'))
v3 = int(input('\033[1;36mEm quantos anos ira pagar: '))

#Imagem#
print('-=-' * 14)
sleep(0.5)
print('Cálculando...')
sleep(1.0)
print('-=-' * 14)
sleep(1.5)

#Contas#
ps = v1 / (v3 * 12)
cf = v2 * 30 / 100

#Decisão#
if ps <= cf:
    print('\033[1;32mImpréstimo concedido!')
    sleep(0.5)
    print('\033[1;32mO válor a pagar por mês será de R${:.2f} Reais.'.format(ps))
    print('\033[1;32mObrigado! e boa compra!')
else:
    print('\033[1;31mInfelismente, você não pode parcelar essa casa.')
    sleep(0.5)
    print('\033[1;31mPor causa que {:.2f} é 30% do seu sálario.\nAs parcelas seriam R${:.2f} !.'.format(cf, ps))
    print('\033[1;31mSentimos muito!, infelismente não podemos deixar passar de 30%.')
