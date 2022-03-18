import math
co = float(input('Qual o comprimento do cateto oposto do triangulo retangulo:'))
ca = float(input('Qual o comprimento do cateto adjacente do triangulo retangulo:'))
h = math.hypot(co, ca)
print('O comprimento da hipotenusa do triangulo retangulo e {:.2f} !'.format(h))
