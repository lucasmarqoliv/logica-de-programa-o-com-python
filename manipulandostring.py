# verificar se nome da cidade começa com 'santo'
cidade = str(input('digite sua cidade: '))
nome_cidade = cidade.startswith('santo')
if nome_cidade == True:
    print ('sua cidade começa com santo.')
else:
    print ('sua cidade não começa com santo.')


