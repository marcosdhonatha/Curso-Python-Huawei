# Exercício Proposto 5.5
# Enunciado: Escreva um programa que leia três números inteiros: LMin, LMax e D. Em seguida exiba na tela todos
# os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].

def main():
    lMin =int(input("Digite LMin: "))
    lMax =int(input("Digite LMax: "))
    d = int(input("Digite D: "))

    print(f"Mostrando todos os numeros no intervalo[{lMin},{lMax}] que são divisíveis por {d}: ")

    for i in range(lMin,lMax+1):
        if i % d == 0:
            print(i)

if __name__=="__main__":
    main()