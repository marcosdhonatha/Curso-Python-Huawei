# Exercício Proposto 5.10
# Enunciado: Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
# Lembrando: um número primo é divisível apenas por 1 e por ele mesmo
from math import sqrt
def main():
    num=int(input("Digite um número natural que deseja verificar se é primo: "))
    cont =0
    for i in range (1, int(sqrt(num))+1):
        if num % i == 0:
            cont+=1

    if cont>1:
        print(f" O número {num} não é primo.")
    else:
        print(f"O número {num} é primo.")
if __name__=="__main__":
    main()