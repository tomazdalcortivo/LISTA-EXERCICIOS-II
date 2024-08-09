n = int(input("Quantos números você vai inserir? "))

soma_pares = 0
contador = 0

while contador < n:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero <= 0:
        print("Por favor, insira apenas números inteiros positivos.")
        continue
    
    if numero % 2 == 0:
        soma_pares += numero
    
    contador += 1

print(f"A soma dos números pares é: {soma_pares}")
