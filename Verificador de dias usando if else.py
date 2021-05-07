dia = int(input('Digite um valor de 1 a 7: '))

if dia > 0 and dia <= 7:
    if dia == 1:
        print('Domingo')
    if dia == 2:
        print('Segunda')
    if dia == 3:
        print('Terça')
    if dia == 4:
        print('Quarta')
    if dia == 5:
        print('Quinta')
    if dia == 6:
        print('Sexta')
    if dia == 7:
        print('Sábado')
else:
    print('Valor inválido')
