#Salário Vendedores
vendedor = type(input("Insira o nome do Vendedor: "))
salario_fixo = float(input("insira o salário fixo "))
total_de_vendas = float(input("Vendas no mês "))
# Valor da comissão por venda
COMISSAO_1 = 1.0 / 100 #Comissão de 1% no total valor das vendas
COMISSAO_2 = 1.5 / 100 #Comissão de 1.5% no valor total das vendas
COMISSAO_3 = 2.0 / 100 #Comissao de 2% no valor total das vendas
if total_de_vendas < 5000:
    comissaoTotal = float(COMISSAO_1 * total_de_vendas)  # 1%
elif total_de_vendas == 5000 or total_de_vendas <= 10000:
    comissaoTotal = float(COMISSAO_2 * total_de_vendas)  # 1,5%
elif total_de_vendas > 10000:
    comissaoTotal = float(COMISSAO_3 * total_de_vendas)  # 2%

# Salário total do vendedor é fixo de 1000 + a comissão sobre o total de vendas do mês
salario_Total = salario_fixo + comissaoTotal
print(f"O salário do vendedor {vendedor} será de { salario_Total}")

#Salário do Gerente
gerente = input("Insira o nome do Vendedor: ")
salario_fixo = float(input("insira o salário fixo "))
total_de_vendas_da_loja = float(input("Vendas no mês "))
#comissão do gerente
COMISSAO_GERENTE = 0.5/100 #comisão do gerente é de 0.5 sobre o total de vendas da loja
salario_gerente = float(COMISSAO_GERENTE * total_de_vendas_da_loja )
salario_total = float(salario_fixo + salario_gerente) # salario fixo é de 2000 + comissão

print(f"O salário do gerente {gerente} será de {salario_total}")


