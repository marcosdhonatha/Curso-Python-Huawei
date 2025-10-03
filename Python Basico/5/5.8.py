# Exercício Proposto 5.8
# Enunciado: Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica
# o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
# Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas
# informações:
# a) O código do produto;
# b) A quantidade vendida desse produto
# O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e
# industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a
# quantidade deve ser ignorada.

def main():

    quantidade = [0,0]


    while True:
        codigo= int(input("Digite o código do produto: "))
        if codigo==0:
            break
        elif codigo != 1 and codigo != 2:
            print("Insira um código válido:\n1 - Residencial\n2 - Industrial: ")
            continue
        quant= int(input("Digite o quantidade: "))
        quantidade[codigo-1]+=quant

    print("\nQuantidade final:\nResidencial: {}\nIndustrial: {} ".format(quantidade[0], quantidade[1]))




if __name__=="__main__":
    main()