nome = str(input('digite seu nome: '))
nome_sem_espacos = nome.replace(' ', '')
print (f'seu nome com letras maiusculas: {nome.upper()}')
print (f'seu nome com letras minusculas: {nome.lower()}')
print (f'quantidade de letras sem considerar espaços: {nome_sem_espacos.__len__()}')
print (f'quantidade de letras tem o primeiro nome: {nome.find(' ')}')
# teste
# teste