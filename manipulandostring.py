# verificar se nome da cidade começa com 'SANTO'
cidade = str(input('digite sua cidade: ')).strip().upper()
cidade = cidade.startswith('SANTO')
if cidade == True:
    print ('sua cidade começa com santo.')
else:
    print ('sua cidade não começa com santo.')


