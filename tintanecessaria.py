largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))
area = largura * altura
tinta = 2
litro = area / tinta
print ('voce precisa de {} lts para pintar uma área de {} m²'.format(litro, area))