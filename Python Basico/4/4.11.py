# Exercício Proposto 4.11:

# No comércio, o conceito de Margem Bruta é uma porcentagem que é aplicada ao preço de custo
# para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
# 45% quando o preço de custo de um produto é menor ou igual a R$ 100,00. Se o produto custa mais
# que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
# mostre na tela qual o seu preço de venda, com duas casas decimais


def main():
    custo = float(input("digite o valor do custo do produto: "))

    preco = 0
    if custo<=100:
        preco =custo + custo*0.45
    else:
        preco = custo + custo*0.35

    print(f"O custo final do produto é {preco:.2f}")


if __name__=="__main__":
    main()