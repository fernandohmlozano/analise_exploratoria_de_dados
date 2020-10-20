linha = input("Dados: ")
dados = linha.split(",")
dados[1] = float(dados[1])
dados[2] = float(dados[2])
if dados[3] == "Sim":
    dados[3] = True
else:
    dados[3] = False
print(dados)