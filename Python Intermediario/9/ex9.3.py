# Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
# de inteiros aleatórios. Exiba a lista na tela. Em seguida elimine valores que estiverem repetidos,
# deixando apenas uma ocorrência de cada. Exiba a nova lista sem repetidos e o seu tamanho.

from random import randint

def main():
    quant = int(input("Digite quantos elementos desejados:"))

    list= []
    for x in range(quant):
        list.append(randint(1,100))

    Set = set(list)
    print(f" O novo tamanho da lista é: {len(Set)}")
    print(Set)

if __name__=="__main__":
    main()