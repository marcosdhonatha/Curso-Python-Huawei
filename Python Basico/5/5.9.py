# Exercício Proposto 5.9
# Enunciado: Escreva um programa que leia um número inteiro N. Em seguida calcule e mostre na tela o fatorial
# de N (N!)

def main():
    n = int(input("Digite o valor de n o qual deseja calcular o fatorial: "))

    fat=1
    for i in range(1,n+1):
        fat*=i
    print("O fatorial de {} é {} ".format(n,fat))
if __name__=="__main__":
    main()