# Exercício Proposto 4.13:

# Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
# primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
# município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
# haverá segundo turno ou não.

def main():
    municipio= input("Digite o nome do municipio: ")
    eleitores=int(input(f"Digite a quantidade de eleitores do municipio {municipio}: "))
    votos= int(input("Digite a quanntidade de votos do candidato mais votado nesse municipio: "))

    if eleitores>200000 and votos<=0.5*eleitores:
        print(f"Haverá segundo turno em {municipio}!")
    else:
        print(f"Não haverá segundo turno em {municipio}!")

if __name__=="__main__":
    main()