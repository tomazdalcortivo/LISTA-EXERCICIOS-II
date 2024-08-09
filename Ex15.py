i = 1
contagem_abaixo_peso = 0 

while i <= 10:
    
    peso = int(input(f"DIgite o peso {i} em kg "))
    altura = float(input(f"DIgite o altura {i} em metros "))

    imc = peso / (altura ** 2)
    
    if imc <= 18.5:
        contagem_abaixo_peso += 1
        
    i += 1 
    
print(f"Quantidade de pessoas abaixo do peso (IMC <= 18,5): {contagem_abaixo_peso}")