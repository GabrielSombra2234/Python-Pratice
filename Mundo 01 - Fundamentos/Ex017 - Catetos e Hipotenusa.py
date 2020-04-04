'''co = float(input('comprimento do cateto oposto< '))
ca = float(input('comprimento do cateto adjaçente< '))
hi = (co**2+ca**2)**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(hi))'''
from math import hypot
co = float(input('comprimento do cateto oposto< '))
ca = float(input('comprimento do cateto adjaçente< '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
