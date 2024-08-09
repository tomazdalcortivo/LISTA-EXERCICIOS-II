n = int(input("Digite o valor de n (quantidade de múltiplos): "))
i = int(input("Digite o valor de i (o múltiplo): "))

contador = 1

while contador <= n:
    multiplo = contador * i
    if contador == n:
        print(multiplo)
    else:
        print(multiplo, end=", ")
    contador += 1
