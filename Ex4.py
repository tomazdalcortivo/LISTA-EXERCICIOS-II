n = int(input("Digite um divisor: "))

i = 1 

while i <= 5:
    valor = int(input(f"Informe o valor {i}: "))
    if valor % n == 0:
        print(F"{valor} é divisivel por {n}")
    i += 1 
