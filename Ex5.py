m = int(input("Informe o valor de m (deve ser maior que n): "))
n = int(input("Informe o valor de n: "))


if m <= n:
    print("O valor de m deve ser maior que n.")
else:

    i = m 

    while i >= n:
        print(i)
        i -= 1 