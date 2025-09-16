# Exercício Proposto 3.7:

# Enunciado: Quando uma pessoa ou uma empresa realiza um investimento espera-se um retorno positivo (lucro),
# embora também possa ocorrer um retorno negativo (prejuízo). Uma forma inicial de avaliar o retorno
# é conhecida com Retorno sobre Investimento (ou ROI, uma sigla em inglês). Cálculo do ROI:

# 𝑅𝑂𝐼 = ((𝑅𝑒𝑐𝑒𝑖𝑡𝑎 − 𝐶𝑢𝑠𝑡𝑜𝑠 + 𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜)/(𝐶𝑢𝑠𝑡𝑜𝑠+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜))*100%

# Escreva um programa que leia 3 dados de entrada reais: Investimento, Custos e Receita, calcule o
# ROI usando a fórmula acima e exiba o resultado com uma casa decimal no formato mostrado abaixo.
# Exemplo: Investimento = 2300.00 – Custos = 345.73 – Receita = 2712,17
# Saída: ROI = 2.5%



def calcula_ROI(invest,custo,receita):
    roi= ((receita-custo-invest)/(custo+invest))*100
    return roi

def main():
    print("##### Programa que calcula ROI ######")
    invest= float(input("Digite o investido: "))
    custo= float(input("Digite o custo: "))
    receita= float(input("Digite o receita: "))

    print(f"ROI = {calcula_ROI(invest,custo,receita):.1f}%")

if __name__ == "__main__":
    main()
