dis = int(input('Qual a distância da viagem? '))
if dis <= 200:
    preço1 = dis * 0.50
    print('Você está prestes a começar uma viagem de {}.'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço1))
else:
    preço2 = dis * 0.45
    print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço2))
    