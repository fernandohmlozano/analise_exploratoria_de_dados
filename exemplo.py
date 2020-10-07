# a = append
# w = cria tabela
# r = le


arquivo = open("exemplo.txt", "r")
arquivo.write("Item | Quantidade\n")
item = input("Qual item? ")

while item !="":
    quantidade = int(input("Quantidade: "))
    arquivo.write("%s | %d\n" %(item,quantidade))
    item = input("Qual item? ")
arquivo.close()