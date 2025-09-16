# Exercício Proposto 3.2:

# Enunciado: Escreva um programa que leia um texto e mostre na tela o texto e a quantidade de caracteres que
# ele contém, usando a seguinte mensagem:
# "O texto {AquiColoqueOTexto} contém {Quantidade} caracteres"
# Faça de dois modos: com o método .format() e com f-string
# Dica Use a função len()

def main():
    texto=input("Digite um texto qualquer: ")
    print(f"O texto <{texto}> contém {len(texto)} caracteres ")
    print("O texto <{}> contém {} caracteres".format(texto, len(texto)))

if __name__ =="__main__":
    main()