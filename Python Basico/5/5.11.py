# Exercício Proposto 5.11
# Enunciado: Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da
# sequência de Fibonacci.
# A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
# são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
# Caso de teste: Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21

def main():
    num=int(input("Digite o valor de n: "))
    seq_fib=[1,1]
    for i in range(2,num+1):
        seq_fib.append(seq_fib[-1]+seq_fib[-2])
    print(seq_fib)
if __name__=="__main__":
    main()