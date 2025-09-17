# Exercício Proposto 5.6
# Enunciado: Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings). Para cada
# cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela
# contém. O programa termina quando for digitado "FIM" (em letras maiúsculas).

def main():
    print("Digite cadeias de caracteres, ao digitar 'FIM' o programa encerra: ")

    while True:
        vetor = input("Digite uma string: ")
        if vetor == "FIM":
            break
        print(f"Você digitou '{vetor}' que contém {len(vetor)} caracteres.:")

if __name__=="__main__":
    main()