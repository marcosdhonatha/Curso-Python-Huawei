# Exercício Proposto 5.12
# Enunciado: Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela os Qtde termos
# da sequência de Fibonacci que sejam maiores que Prim.

## Percebo um erro nesse enunciado. Para qualquer numero real n sempre existiram infinitos termos da sequência fibonacci
## que são maiores que n, pois essa é uma série infinita.

# Vou modificar o enunciado e resolver conforme nova especificação:

#Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela a quantidade Qtde de termos
# da sequência de Fibonacci que sejam maiores que Prim.
def fib(quant, prim):
    seq=[1,1]

    i=1
    cont=0
    while True:

        if seq[i]>prim:
            cont+=1
            if cont==quant:
                break
        seq.append(seq[i-1]+seq[i-2])
        i+=1
    print(seq[i-cont+1:])



def main():
        quant=int(input("Insira a quantidade de termos: "))
        prim=int(input("Insira o primeiro número a partir do qual se iniciará a seq de fib: "))

        fib(quant,prim)

if __name__=="__main__":
    main()