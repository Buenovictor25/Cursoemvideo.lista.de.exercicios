nome = str(input('Digite o seu nome completo:')).strip()
print('Analisando o seu nome...')
print('Seu nome com as letras MAIUSCULAS: {}'.format(nome.upper()))
print('Seu nome em letras minusculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras !'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras !'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras !'.format(separa[0], len(separa[0])))









