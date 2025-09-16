# Exercício Proposto 4.12:

# Leia um número inteiro entre 1 e 12 e exiba o mês correspondente. Caso seja digitado um número
# fora desse intervalo, o programa deve exibir uma mensagem informando que não existe mês com
# este número


def main():
    meses={
        1:"Janeiro",
        2:"Fevereiro",
        3: "Março",
        4:"Abril",
        5:"Maio",
        6:"Junho",
        7:"Julho",
        8:"Agosto",
        9:"Setembro",
        10:"Outubro",
        11:"Novembro",
        12:"Dezembro"
    }
    mes=int(input("Digite o número correspondente ao mês[1-12]: "))
    if mes not in meses:
        print("Esse mês não existe!")
    else:
        print(f"O mês {mes} é o mês {meses[mes]}")

if __name__=="__main__":
    main()