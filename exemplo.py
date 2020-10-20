# a = append acrescenta e não perde o que tem
# w = cria tabela do zero e perde o que já tem
# r = le o arquivo


arquivo = open("exemplo.txt", "r")
arquivo.write("Item | Quantidade\n")
item = input("Qual item? ")

while item !="":
    quantidade = int(input("Quantidade: "))
    arquivo.write("%s | %d\n" %(item,quantidade))
    item = input("Qual item? ")
arquivo.close()