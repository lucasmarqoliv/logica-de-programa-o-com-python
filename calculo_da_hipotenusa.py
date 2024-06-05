import math
cateto_oposto = float(input('digite o cateto oposto: '))
cateto_adjascente = float(input('digite o cateto adjascente: '))
resultado = math.hypot(cateto_oposto,cateto_adjascente)
print ('a hipotenusa das dimensões informadas é igual a {}'.format(resultado))