primeiro_termo = int(input("Digite o primeiro termo da PG: "))
razao = int(input("Digite a razão da PG: "))
ultimo_termo = int(input("Digite o último termo da PG: "))

termo_atual = primeiro_termo
soma = 0

while termo_atual <= ultimo_termo:
    soma += termo_atual
    termo_atual *= razao

print(f'A soma dos termos da progressão geométrica é: {soma}')