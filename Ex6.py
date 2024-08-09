num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# ve pela função de max e min quais dos valores são maiores e menore para o intervalo
inicio = min(num1, num2)
fim = max(num1, num2)

i = inicio + 1


print(f"Números pares entre {inicio} e {fim}:")

while i < fim:
    if i % 2 == 0:  
        print(i)
    i += 1 