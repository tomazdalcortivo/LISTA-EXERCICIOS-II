i = 1
contador_negativo = 0 

while i <= 10:
    valor = int(input(f"informe o valor {i}: "))
    if valor < 0:
        contador_negativo += 1 
    i += 1 

print(F"Quantidade de valores negativos: {contador_negativo}")
        