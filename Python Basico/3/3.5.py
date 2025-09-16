# Exercício Proposto 3.5:

# Enunciado: Escreva um programa que leia um número inteiro que representa uma quantidade de tempo em
# segundos. Calcule e mostre na tela a quantidade de horas, minutos e segundos.
# Dicas: Leve em consideração que 1 hora tem 3600 segundos e 1 minuto tem 60 segundos.
# Use os operadores de divisão de inteiros (//) e resto (%).

def main():
    segundos= int(input("Digite um numero inteiro representando uma quantidade de segundos: "))

    horas=segundos//3600
    minutos = (segundos - horas * 3600) // 60
    segundos_quebrados=segundos-(horas*3600)- minutos*60

    print(f"{segundos} segundos são: ")
    print(f"{horas} hora(s), {minutos} minuto(s), {segundos_quebrados} segundo(s)")
if __name__ == "__main__":
    main()