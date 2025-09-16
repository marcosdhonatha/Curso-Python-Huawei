# Exercício Proposto 4.7:

# Em Albalândia mulheres e homens podem servir o exército do país. O serviço é opcional e é muito
# comum que as pessoas se apresentem para o serviço em algum momento da vida. Existe uma única
# restrição para ingresso que é a idade da pessoa: para mulheres a idade aceita é entre 21 e 34 anos;
# para homens a idade aceita é entre 18 e 39 anos. Escreva um programa que leia três dados de
# entrada: nome da pessoa, idade e sexo e informe se a pessoa será aceita ou não para o serviço.
# Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou 'F' para feminino e 'm' ou 'M'
# para masculino, qualquer coisa diferente deve ser informado como inválido.

def main():
    nome= input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo= input("Digite o sexo da pessoa: ").upper()


    idade_homem = list(range(18,40))
    idade_mulher = list(range(21,35))

    if sexo=="M":
        if idade in idade_homem:
            print(f"O homem {nome} foi aceito no serviço militar!")
        else:
            print(f"O homem {nome} foi foi recusado no serviço militar")

    elif sexo=="F":
        if idade in idade_mulher:
            print(f"A mulher {nome} foi aceita no serviço militar!")
        else:
            print(f"A mulher {nome} não foi aceita no serviço militar")
if __name__=="__main__":
    main()