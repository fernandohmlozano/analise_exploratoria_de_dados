with open("exemplo.txt", "r") as file:
    for i in file:
        print(i)
if file.close:
    print("Arquivo fechado")
else:
    print("Arquivo aberto")