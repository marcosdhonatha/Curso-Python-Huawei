# Exercício Proposto 3.1:
#
# Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança. O
# programa deve exibir na tela a mensagem.
# "Os adultos {mãe} e {pai} são os responsáveis por {criança}"
# Faça de dois modos: com o método .format() e com f-string


def using_fstring(pai, mae, crinca):
    print(f"\nOs adultos {pai} e {mae} são os responsáveis por {crinca}")

def using_format(pai, mae, crianca):
    print("Os adultos {} e {} são os responsáveis por {}".format(pai, mae, crianca))
def main():

    pai = input("Digite o nome do pai:")
    mae = input("Digite o nome da mãe:")
    crianca = input("Digite o nome da crinça:")

    using_fstring(pai, mae, crianca)
    using_format(pai, mae, crianca)
    # use_format()


if __name__ == '__main__':
    main()


