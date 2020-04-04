sd1=str(input('Qual o nome da sua cidade ?: ')).strip().title()
sd2=sd1.split()
print('{}, Essa cidade começa com Santo: {}.'.format(sd1,'Santo'in sd2[0]))
