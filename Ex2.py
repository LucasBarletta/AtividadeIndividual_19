telefone = input('Digite numero de telefone ')

if len(telefone) == 9 and telefone[0] == '9':
    print('Número valido')
else:
    print('Numero invalido')