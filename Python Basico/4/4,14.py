# Exercício Proposto 4.14:

# Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
# Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
# Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
# quer comprar e calcule o valor em reais necessários.

def main():
    dolar=4.89
    euro=5.26
    libra=6.17
    moedas=['D', 'E', 'L']

    print("Informe qual moeda deseja comprar:")
    print("'D' - Dólar\n'E' - Euro\n'L' - Libra")
    moeda = input("Moeda: ")

    if moeda not in moedas:
        print("Escolha uma moeda válida!")
        exit(1)

    valor = float(input("Digite a quantidade da moeda selecionada que deseja comprar: "))

    if moeda == "D":
        print(f"Para comprar {valor} dólares você precisará de {dolar*valor:.2f} reais!")
    elif moeda == "E":
        print(f"Para comprar {valor} euros você vai precisar de {euro*valor:.2f} reais!")
    else:
        print(f"Para comprar {valor} libras esterlinas você precisará de {libra*valor:.2f} reais!")
if __name__=="__main__":
    main()