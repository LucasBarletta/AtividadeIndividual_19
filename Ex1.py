numero = [9,8,7,1,4,6,7,8,9]
digitar = int(input('Digite 1 para impar e 2 para par: '))

def par(numero):

    for n in numero:
        if n % 2 == 0:
            print(n)
    return numero

def impar(numero):

    for n in numero:
        if n % 2 != 0:
            print(n)
    return numero

def digi():
    if digitar == 1:
        impar(numero)
    else:
        par(numero)
digi()
