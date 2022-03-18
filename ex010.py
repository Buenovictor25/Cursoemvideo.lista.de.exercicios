print('-----Desafio 10-----')

n = float(input('Digite o valor que se encontra na sua conta bancaria. R$'))
d = n / 5.16
e = n / 5.54
y = n / 0.80
i = n / 0.044
l = n / 6.70
print('Voce tem {:.2f} reais na sua conta, e isso pode comprar {:.2f} dolares na cotaçao atual !'.format(n, d))
print('Com R${:.2f} na conta voce consegue comprar {:.2f} euros!'.format(n, e))
print('Com R${:.2f} na conta voce consegue comprar {:.2f} yuan chines!'.format(n, y))
print('Com R${:.2f} na conta voce consegue comprar {:.2f} ienes!'.format(n, i))
print('Com R${:.2f} na conta voce consegue comprar {:.2f} libras esterlinas!'.format(n, l))



