# Exercício Proposto 5.2
# Enunciado: Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis
# por 7 entre 1 e N (inclusive).

def main():
    num=int(input("Digite um numero: "))

    for i in range(1,num+1):
        if i%7==0:
            print(i)
if __name__=="__main__":
    main()