termo1 = termo2 = 1
contador = 2

print(termo1)
print(termo2)

while contador < 20:
    termo_atual = termo1 + termo2
    print(termo_atual)
    termo1 = termo2
    termo2 = termo_atual
    contador += 1
