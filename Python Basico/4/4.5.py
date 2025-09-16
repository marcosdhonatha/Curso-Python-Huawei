# Exercício Proposto 4.5:

# Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
# a) menor que 16 anos -> não eleitor
# b) entre 18 completos e 65 anos incompletos -> eleitor obrigatório
# c) entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo

def main():
    idade=int(input("Digite a idade da pessoa: "))

    if idade>=18 and idade <= 65:
        print("Eleitor obrigatório ")
    elif (idade >= 16 and idade < 18) or idade > 65:
        print("Eleitor facultativo")
    else:
        print("Não eleitor ")

if __name__ =="__main__":
    main()