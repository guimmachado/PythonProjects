base = int(input('Digite a base: '))
expo = int(input('Digite o expoente: '))

cont = 0
prod = 1
while cont < expo:
    prod = prod * base
    cont = cont + 1

print(base, 'elevado a', expo, '=', prod)
