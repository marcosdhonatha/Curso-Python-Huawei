# Exercício Proposto 3.3:

# Enunciado: Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa
# deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais.
#
# R1 = (a+b+c)
# R2 = (a*b*c)
# R3 = (2*(a+b))
# R4 = ((a+b+c)/3)
# R5 = ((2*b+3*c)/5*a)
# R6 = (a**2 + b**2)

def formulas(a, b, c):
    R1 = (a+b+c)
    R2 = (a*b*c)
    R3 = (2*(a+b))-c
    R4 = ((a+b+c)/3)
    R5 = (((2*b)+(3*c))/(5*a))
    R6 = (a**2 + b**2)

    print(f"Resultado da fórmula R1: {R1:.3f}" )
    print(f"Resultado da fórmula R2: {R2:.3f}" )
    print(f"Resultado da fórmula R3: {R3:.3f}" )
    print(f"Resultado da fórmula R4: {R4:.3f}" )
    print(f"Resultado da fórmula R5: {R5:.3f}" )
    print(f"Resultado da fórmula R6: {R6:.3f}" )





def main():
    print("Digite três número reais:")
    a = float(input("Numero real a: "))
    b = float(input("Numero real b: "))
    c = float(input("Numero real c: "))

    formulas(a,b,c)
if __name__ == "__main__":
    main()