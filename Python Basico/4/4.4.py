# Exercício Proposto 4.4:

# Enunciado: Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações. A média
# final é a média aritmética das três notas e a pessoa estará aprovada se essa média for maior ou igual
# a 7.0. Mostre na tela o nome, a média e a situação que será "Aprovado" ou "Reprovado"

def main():

    nome= input("Digite o nome do aluno: ")
    nota1= float(input("Digite sua nota 1: "))
    nota2= float(input("Digite sua nota 2: "))
    nota3= float(input("Digite sua nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print(f"O aluno {nome} foi aprovado com média {media:.2f}!")
    else:
        print(f"O aluno {nome} não foi aprovado pois obeteve média {media:.2f}!")

if __name__ =="__main__":
    main()