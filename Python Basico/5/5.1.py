# Exercício Proposto 5.1:

# Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro
# do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo
# manter o programa correto, totalizando e contando os valores diferentes de zero que forem
# digitados.
# Dica: a solução consiste em alterar a ordem dos comandos existentes dentro do laço while

def main():
    soma = qtde = 0
    A = int(input("Digite X: "))
    while A != 0:
        soma = soma + A
        qtde = qtde + 1
        A = int(input("Digite X: "))

    print(f'Soma dos valores = {soma}')
    print(f'Quantidade = {qtde}')
    print('Fim do Programa')
if __name__=="__main__":
    main()