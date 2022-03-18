'''import math
an = float(input('Digite o angulo que voce deseja:'))
s = math.sin(math.radians(an))
print('O angulo de {} em seno equivale a {:.2f} !'.format(an, s))
c = math.cos(math.radians(an))
print('O angulo de {} em cosseno equivale a {:.2f}'.format(an, c))
t = math.tan(math.radians(an))
print('O angulo de {} em tangente equivale a {:.2f}'.format(an, t))'''
from math import sin,cos,tan,radians

an = float(input('Digite o angulo que voce deseja:'))
s = sin(radians(an))
print('O angulo de {} em seno equivale a {:.2f} !'.format(an, s))
c = cos(radians(an))
print('O angulo de {} em cosseno equivale a {:.2f}'.format(an, c))
t = tan(radians(an))
print('O angulo de {} em tangente equivale a {:.2f}'.format(an, t))



