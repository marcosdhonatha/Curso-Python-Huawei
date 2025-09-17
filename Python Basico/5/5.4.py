# Exercício Proposto 5.4
# Enunciado: Escreva um programa que leia dois números inteiros: LMin e LMax. Em seguida exiba na tela todos
# os valores dentro do intervalo fechado [LMin, LMax].


def main():
    num=int(input("Digite um numero: "))
    num2=int(input("Digite outro numero: "))

    for i in range(num,num2+1):
        print(i)
if __name__=="__main__":
    main()