m = float(input('Digite um número em métros<'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(' A media me km é {}km, \n em hm é {}hm, \n em dam é {}dam, \n em dm é {:.0f}dm, \n em cm é {:.0f}cm, \n em mm é {:.0f}mm'.format(km, hm, dam, dm, cm, mm))
