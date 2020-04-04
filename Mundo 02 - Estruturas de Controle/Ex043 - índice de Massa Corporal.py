#Bibliotécas#
from time import sleep

#Prints#
print('-' * 20)
sleep(0.3)
print('Teste de IMC')
sleep(0.4)
print('*IMC = Indíce de Massa Corpória*')
sleep(0.4)
print('-' * 20)
sleep(0.3)

#Variáveis#
altura = float(input('Quanto Você Tem de Altura (M): '))
peso = float(input('Quanto Você Pesa (Kg): '))
resultado = peso / (altura ** 2)

#Estruturas de controle#
if resultado <= 18.5:
    print('Abaixo do Peso! {:.1f}'.format(resultado))
elif 18.5 <= resultado < 25:
    print('Peso Ideal! {:.1f}'.format(resultado))
elif 25 <= resultado < 30:
    print('Sobrepeso! {:.1f}'.format(resultado))
elif 30 <= resultado < 40:
    print('Obesidade! {:.1f}'.format(resultado))
else:
    print('Obesidade Mórbida! {:.1f}'.format(resultado))
