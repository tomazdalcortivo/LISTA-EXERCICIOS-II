primeiro_termo = int(input("Digite o primeiro termo da série de Ricci: "))
segundo_termo = int(input("Digite o segundo termo da série de Ricci: "))
n = int(input("Digite o número de termos a serem gerados: "))

if n <= 0:
    print("O número de termos deve ser maior que 0.")
elif n == 1:
    print(f"Série de Ricci: {primeiro_termo}")
elif n == 2:
    print(f"Série de Ricci:\n{primeiro_termo}\n{segundo_termo}")
else:
    print(f"Série de Ricci:")
    print(f"{primeiro_termo}")
    print(f"{segundo_termo}")

    termo1 = primeiro_termo
    termo2 = segundo_termo

    contador = 2  

    while contador < n:
        proximo_termo = termo1 + termo2
        print(f"{proximo_termo}")
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1
