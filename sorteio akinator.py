from random import randint
def numero_aleatorio():
    aleatorio=randint(1,10)
chute=0
while numero_aleatorio() != chute:
    chute = int(input('digite um valor(1 a 10'))
    if (numero_aleatorio == chute):
        print('parabens voce acertou')
    else:
        print('tente novamente')
        numero_aleatorio()











