# Exercício Proposto 3.6:

# Enunciado: Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos
# mais comissão de 6% sobre o valor total vendido no mês. Escreva um programa que leia o nome e o
# total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saída conforme o exemplo
# a seguir. Exiba os valores numéricos com duas casas decimais.
# Exemplo vendedor José Carlos Santos vendeu R$ 43759.35 e faz jus a uma comissão de R$ 3825.56
# de saída: vendedor Manoel Guimarães vendeu R$ 61417.81 e faz jus a uma comissão de R$ 4885.07
# vendedor Plínio Pereira vendeu R$ 39336.87 e faz jus a uma comissão de R$ 3560.21

def main():
    vend1= input("digite o nome do vendedor 1: ")
    vend1_Total =  float(input(f"Digite o total vendido pelo vendedor {vend1}: "))
    vend2= input("digite o nome do vendedor 2: ")
    vend2_Total =  float(input(f"Digite o total vendido pelo vendedor {vend2}: "))
    vend3= input("digite o nome do vendedor 3: ")
    vend3_Total = float(input(f"Digite o total vendido pelo vendedor {vend3}: "))

    print(f"O vendedor {vend1} vendeu R${vend1_Total} e faz jus a uma comissão de R${vend1_Total*0.06+1200:.2f}")
    print(f"O vendedor {vend2} vendeu R${vend2_Total} e faz jus a uma comissão de R${vend2_Total*0.06+1200:.2f}")
    print(f"O vendedor {vend3} vendeu R${vend3_Total} e faz jus a uma comissão de R${vend3_Total*0.06+1200:.2f}")


if __name__ == "__main__":
    main()