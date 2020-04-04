print('\033[1;32m=-' * 8)
#Colocando as notas.
NT1 = float(input('Pimeira nota: '))
NT2 = float(input('Segunda Nota: '))
print('-=' * 8)
MD = (NT1 + NT2) / 2
print('Tirando {:.1f} e {:.1f} a sua média {:.1f} .'.format(NT1, NT2, MD))
#Programando o if
if 7 > MD >= 5:
    print('Com média {:.1f} o aluno está de [RECUPERAÇÃO]. '.format(MD))
elif MD < 5:
    print('Com a média {:.1f} o aluno está [REPROVADO]. '.format(MD))
else:
    print('Com a média de {:.1f} o aluno está [APROVADO]. '.format(MD))
