# Exercício Proposto 4.10:

# Escreva um programa que leia 3 números inteiros e mostre na tela se eles formam um triângulo ou
# não. Caso formem um triângulo informe o tipo de triângulo (equilátero, isósceles ou escaleno).
# Regra: Para três números formarem um triângulo precisa ocorrer que:
# a) os três números precisam ser maiores que zero;
# b) a soma dos dois menores valores deve ser maior que o terceiro.

def tipo_triangulo(medidas):
    if medidas[0]==medidas[1] and medidas[1]==medidas[2]:
        return "Equilátero"
    elif medidas[0]==medidas[1] or medidas[1]==medidas[2] or medidas[2]==medidas[0]:
        return "Isóceles"
    else:
        return "Escaleno"

def main():
    medidas=[]
    medidas.append(int(input("Digite o tamanho do lado A: ")))
    medidas.append(int(input("Digite o tamanho do lado B: ")))
    medidas.append(int(input("Digite o tamanho do lado C: ")))

    medidas.sort()

    if medidas[0]==0 or (medidas[0]+medidas[1]<=medidas[2]):
        print("Essas não são medidas de um triângulo válido")
    else:
        print(f"Essas são medidas de um triangulo do tipo {tipo_triangulo(medidas)}")



if __name__==("__main__"):
    main()