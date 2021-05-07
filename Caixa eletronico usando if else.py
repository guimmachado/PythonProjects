saque = int(input('Digite o valor do saque: '))

if 10 <= saque <= 600:
    cem = saque // 100
    saque = saque % 100

    cinquenta = saque // 50
    saque = saque % 50

    dez = saque // 10
    saque = saque % 10

    cinco = saque // 5
    saque = saque % 5

    um = saque // 1

    if cem > 0:
        print(cem, "notas de R$100")
    if cinquenta > 0:
        print(cinquenta, "notas de R$50")
    if dez > 0:
        print(dez, "notas de R$10")
    if cinco > 0:
        print(cinco, "notas de R$5")
    if um > 0:
        print(um, "notas de R$1")
else:
    print("Não foi possível fazer o saque")