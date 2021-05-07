import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print ('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))
