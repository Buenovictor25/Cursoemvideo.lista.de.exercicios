print('-----Desafio 11-----')

pl = float(input('Digite a largura da parede que voce vai pintar:'))
pa = float(input('Digite a altura da parede que voce vai pintar:'))
a = pl * pa
print('A sua parede tem a dimensao de {}x{} e a sua area e de {:.2f} metros quadrados'.format(pl, pa, a))
tinta = a / 2
print('Para pintar essa  parede voce precisara de {} litros de tinta'.format(tinta))


