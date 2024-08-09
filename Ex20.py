total_de_graos = 0
graos_na_casa = 1
numero_da_casa = 1

while numero_da_casa <= 64:
    total_de_graos += graos_na_casa
    graos_na_casa *= 2
    numero_da_casa += 1

print(f'A quantidade total de grãos de milho no tabuleiro de xadrez é: {total_de_graos}')
