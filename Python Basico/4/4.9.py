# Exercício Proposto 4.9:

# Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
# a) "Os três valores são iguais"
# b) "Há dois valores iguais e um diferente"
# c) "Os três valores são diferentes"

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int (input("Digite o terceiro número: "))

    if num1==num2 and num3==num2 :
        print("Todos os números são iguais")
    elif num1==num2 or num2==num3 or num3==num1:
        print("Existem dois números iguais e um diferente")
    else:
        print("Todos os números são diferentes")

if __name__=="__main__":
    main()