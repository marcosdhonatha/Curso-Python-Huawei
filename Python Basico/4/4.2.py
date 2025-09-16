# Exercício Proposto 4.2:

# Enunciado: Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.

def main():
    num= int(input("Digite um número inteiro: "))

    if num%10==0:
        print(f"O número {num} é divisível por 10!")
    else:
        print(f"O número {num} não é divisível por 10!")

if __name__=="__main__":
    main()