frase = str(input('Informe aqui a sua frase:')).upper().strip()
print('A letra A, aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra, A apareceu na posiçao {}'.format(frase.find('A')+1))
print('A ultima letra A, apareceu na posiçao {}'.format(frase.rfind('A')+1))
