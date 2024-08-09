quantidade_positivos = 0
quantidade_negativos = 0

i = 1

while i <= 20:
    valor = int(input(f"Digite o valor {i}: "))
    
    if valor < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1
    
    i += 1

print(f"Quantidade de valores positivos: {quantidade_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")
