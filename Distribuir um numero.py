num = int(input('Digite um número: '))
aux = num
if num <= 1000:

    centenas = aux // 100
    aux = aux % 100

    dezenas = aux // 10
    aux = aux % 10

    unidades = aux // 1

    if num >= 100:
        if centenas > 1:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidade")
        else:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=", centenas, "centena,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centena,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=", centenas, "centena,", dezenas, "dezena e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centena,", dezenas, "dezena e", unidades, "unidade")
    elif 10 <= num < 100:
        if dezenas > 1:
            if unidades > 1:
                print(num, "=", dezenas, "dezenas e", unidades, "unidades")
            else:
                print(num, "=", dezenas, "dezenas e", unidades, "unidade")
        else:
            if unidades > 1:
                print(num, "=", dezenas, "dezena e", unidades, "unidades")
            else:
                print(num, "=", dezenas, "dezena e", unidades, "unidade")
    else:
        if unidades > 1:
            print(num, "=", unidades, "unidades")
        else:
            print(num, "=", unidades, "unidade")
else:
    print('O número é maior ou igual a mil, o programa não po de ser executado.')