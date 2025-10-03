# Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros
# aleatórios dentro do intervalo fechado [1, 50]. Mostre o conjunto gerado na tela.
# Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números
# aleatórios pode representar um problema. Como resolver isso?
# Cuidado: Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior
# que 50. Faça o teste e depois responda a pergunta: por que isso ocorre?

from random import randint

def main():
    quant = int(input("Digite a quantidade de elementos: "))
    conjunto=set()
    for i in range(quant):
        conjunto.add(randint(1,50))
    print(conjunto)
if __name__=="__main__":
    main()