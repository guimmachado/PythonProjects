'''
num = int(input('Digite um número: '))
i, j, k = 1, 2, 3

while i * j * k < num:
    i += 1
    j += 1
    k += 1
if i * j * k == num:
    print(num, 'é triangular.')
else:
    print(num, 'não é triangular.')
'''
n = int(input('Digite o número de pessoas: '))

cont = 0

while