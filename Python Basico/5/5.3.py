# Exercício Proposto 5.3
# Enunciado: Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado
# [100, 200]. Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido
# e permanecer no laço. Quando um valor válido for fornecido o programa deve informar que o valor
# foi aceito e terminar


def main():
    while True:
        num=int(input("Digite um numero: "))
        if num >=100 and num <= 200:
            print("Numero válido!")
            break
        else:
            print("Numero inválido, tente novamente.")
if __name__=="__main__":
    main()