# Exercício Proposto 3.4:

# Enunciado: Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do
# valor lido usando o formato com 3 casas decimais mostrado abaixo:
# Exemplo Valor lido: 136.7
# Exibir 25% -> 34.175 - 50% -> 68.350 - 75% -> 102.525

def main():
    a= float(input("Digite um numero real: "))
    print(f"25% de {a} = {a*0.25:.3f}")
    print(f"50% de {a} = {a*0.50:.3f}")
    print(f"75% de {a} = {a*0.75:.3f}")


if __name__ =="__main__":
    main()