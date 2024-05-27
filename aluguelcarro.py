km = float(input('quanto quilometros voce percorreu? '))
dias = int(input('quantos dias voce esteve com o carro alugado? '))
pago = (km * 0.15) + (dias * 60)
print ('voce deve pagar R$ {:.2f}' .format(pago))
