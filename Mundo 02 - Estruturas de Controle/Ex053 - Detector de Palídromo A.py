from time import sleep
print('''Exemplos:
1¬ APOS A SOPA
2¬ A  SACADA DA CASA
3¬ A TORRE DA DERROTA
4¬ O LOGO AMA O BOLO
5¬ ANOTARAM A DATA DA MARATONA''')
sleep(1)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
