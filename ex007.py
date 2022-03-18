n1 = float(input('Digite a sua nota do primeiro bimestre:'))
n2 = float(input('Digite a sua nota do segundo bimestre:'))
n3 = float(input('Digite a sua nota do terceiro bimestre:'))
n4 = float(input('Digite a sua nota do quarto bimestre:'))
s = (n1 + n2 + n3 + n4) /4

print('A media entre as notas do seu ano letivo: Primeiro bimestre {}\n'
      'Segundo bimestre: {}\n'
      'Terceiro bimestre: {}\n'
      'E quarto bimestre: {} equivale a uma media de {} !'.format(n1,n2,n3,n4,s))

