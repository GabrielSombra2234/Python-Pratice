import math
ângulo=float(input('Digite um ângulo: '))
seno=math.sin(math.radians(ângulo))
print('O seno do ângulo {} é {:.2f}'.format(ângulo, seno))
cosseno=math.cos(math.radians(ângulo))
print('O cosseno do ângulo {} é {:.2f}'.format(ângulo, cosseno))
tângente=math.tan(math.radians(ângulo))
print('A tângente do ângulo {} é {:.2f}'.format(ângulo, tângente))
