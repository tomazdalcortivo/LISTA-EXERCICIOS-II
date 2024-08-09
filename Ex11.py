soma = 0
contador = 0

while True:
    valor = float(input("Digite um valor (ou um número negativo para terminar): "))
    
    if valor < 0:
        break
    
    soma += valor
    contador += 1

if contador > 0:
    
    media = soma / contador
    print(f"A média aritmética dos valores lidos é: {media:.2f}")
else:
    print("Nenhum valor válido foi inserido.")
