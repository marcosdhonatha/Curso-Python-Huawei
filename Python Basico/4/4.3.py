# Exercício Proposto 4.3:

# Enunciado: Uma empresa financeira concede empréstimos a pessoas físicas quando o valor da parcela é menor
# que 8% do salário da pessoa. Escreva um programa que leia dois números reais: o valor do salário e
# o valor da parcela e informe se o empréstimo será concedido ou não.

def main():
    salario= float(input("Digite o valor do seu salário: "))
    parcela= float(input("Digite o valor do seu parcela: "))

    if parcela < salario*0.08:
        print("Seu empréstimo foi liberado!")
    else:
        print("Infelizmente não foi possível liberar seu empréstimo!")

if __name__== "__main__":
    main()