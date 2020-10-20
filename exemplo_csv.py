# def arqcsv():
#    file = open("alunos.csv","a")
#    #file.write("Aluno, Nota Trabalho, Nota Prova, Reprovado/Aprovado\n")
#    nome = input("Nome do aluno: ")
#    while nome != "":
#        trab = float(input("Digite a nota do trabalho: "))
#        prova = float(input("Digite a nota da prova: "))
#        rf = input("Reprovado por falta: ")
#        file.write("%s, %.1f, %.1f,%s\n" % (nome,trab,prova,rf))
#        print("-"*20)
#        nome = input("Nome do aluno: ")
#
# arqcsv()

def lercsv():
    lista = []
    file = open("alunos.csv", "r")
    for linha in file:
        #linha = linha.rstrip()
        aluno = linha.split(",")
        aluno[1] = float(aluno[1])
        aluno[2] = float(aluno[2])
        if (aluno[3] == "True"):
            aluno[3] = True
        else:
            aluno[3] = False
        lista.append(aluno)
    print(lista)
    file.close()


lercsv()

