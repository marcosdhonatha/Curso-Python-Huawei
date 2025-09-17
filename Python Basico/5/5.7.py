# Exercício Proposto 5.7
# Enunciado: Escreva um programa que permaneça em laço lendo quantidades (números inteiros) de produtos
# vendidos. O laço termina quando for digitado zero ou um valor negativo. Ao término do laço exiba na
# tela a soma de todas as quantidades digitadas (se for digitado um negativo para sair do laço ele não
# deve afetar o total)

def main():
    quantidade=0
    while True:
        quant=int(input("Digite a quantidade: "))
        if quant <=0:
            break
        else:
            quantidade+=quant
    print("A quantidade total de produtos vendidos  foi: {}".format(quantidade))

if __name__== "__main__":
    main()