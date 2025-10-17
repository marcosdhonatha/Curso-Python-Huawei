# Escreva um programa que leia do teclado dois conjuntos de números inteiros digitados pelo usuário.
# Exiba na tela a união e a interseção desses conjuntos.

def add_elements(setX):
    print("Digite '0' para sair da função de adicionar elementos")

    while True:
        num=int(input("Digite um elemento:"))
        if num==0:
            break
        else:
            setX.add(num)
    return set


def main():
    setA= set()
    add_elements(setA)
    setB= set()
    add_elements(setB)

    setUnion=setA.union(setB)
    setIntersection=setA.intersection(setB)
    print(setUnion)
    print(setIntersection)








if __name__=="__main__":
    main()