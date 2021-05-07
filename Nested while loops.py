'''
i = 0
n = 5

while i < n:
        j = 0
        while j < n:
            print(i, j)
            j = j + 1
        i = i  + 1
'''
n = int(input('Digite o número de empresas: '))
m = int(input('Digite o número de meses: '))

empresa = 1
print('')
while empresa <= n:
    mes = 1
    balanca = 0
    print('Empresa {}:'.format(empresa))
    while mes <= m:
        print('Mês {}:'.format(mes))
        ganho = int(input('Digite o ganho da empresa no mês: '))
        gasto = int(input('Digite o gasto da empresa no mês: '))
        balanca = balanca + (ganho - gasto)
        print('')
        mes = mes + 1
    if balanca == 0:
        print('A empresa {} ficou indiferente(balança: R$0) '.format(empresa))
    elif balanca > 0:
        print('A empresa {} fechou com lucro de R${}.'.format(empresa, balanca))
    else:
        print('A empresa {} fechou com défict de R${}.'.format(empresa, balanca))
    empresa = empresa + 1
    print('')
         