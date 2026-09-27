
EXCELENTE = 0
BOM = 0 
RUIM = 0

for i in range(10):
    nome_cliente = input("Digite o nome do cliente: ")
    idade_cliente = int(input("Digite a idade do cliente: "))
    pesquisa_avaliacao = int(input("Avalie o atendimento - DIGITE: 1 PARA EXCELENTE / 2 PARA BOM / 3 PARA RUIM: "))

    if pesquisa_avaliacao == 1:
        EXCELENTE +=  1 

    elif pesquisa_avaliacao == 2:
        BOM += 1

    elif pesquisa_avaliacao == 3:
        RUIM += 1

    else: 
        print(f"Valor {pesquisa_avaliacao} é inválido! Digite 1, 2 ou 3.")
        

print(f"Olá, houve {EXCELENTE} votos EXCELENTES ⭐ e {RUIM} votos RUINS 👎") 