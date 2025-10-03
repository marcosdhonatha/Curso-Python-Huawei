# Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
# número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
# número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido".


# LL Linha de calçados
# 16 Bebê
# 49 Masculino esportivo
# 23 Infantil feminino
# 52 Feminino formal salto baixo
# 25 Infantil masculino
# 53 Feminino formal salto alto
# 29 Infantil esportivo
# 55 Feminino casual salto baixo
# 42 Masculino formal
# 56 Feminino casual salto alto
# 43 Masculino casual
# 59 Feminino esportivo


def main():
    ll=int(input("Digite o número do código do calçado: "))

    match ll:
        case 16:
            print("Bebê ")
        case 49:
            print("Masculino esportivo")
        case 23:
            print("Infantil feminino ")
        case 52:
            print("Feminino formal salto baixo")
        case 25:
            print("Infantil masculino ")
        case 53:
            print("Feminino formal salto alto")
        case 29:
            print("Infantil esportivo ")
        case 55:
            print("Feminino casual salto baixo")
        case 42:
            print("Masculino formal ")
        case 56:
            print("Feminino casual salto alto")
        case 43:
            print("Masculino casual ")
        case 59:
            print("Feminino esportivo")
        case _:
            print("Calçado não encontrado!")
if __name__== "__main__":
    main()
