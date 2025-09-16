# Exercício Proposto 4.6
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
    codigo_calcado ={
        16:   "Bebê",
        49:  "Masculino esportivo",
        23:  "Infantil feminino",
        52:  "Feminino formal salto baixo",
        25 : "Infantil masculino",
        53 : "Feminino formal salto alto",
        29 : "Infantil esportivo",
        55 : "Feminino casual salto baixo",
        42 : "Masculino formal",
        56 : "Feminino casual salto alto",
        43 : "Masculino casual",
        59 : "Feminino esportivo"}

    codigo=int(input("Digite o codigo LL do calçado que deseja: "))

    if codigo in codigo_calcado:
        print(codigo_calcado[codigo])
    else:
        print("Calçado não encontrado")

if __name__ =="__main__":
    main()