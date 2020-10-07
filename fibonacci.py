def fib(n):
    txt = open("fibonacci.txt", "w")
    p = 1
    s = 1
    if (n==1):
        txt.write("%d\n" %p)
    elif (n==2):
        txt.write("%d\n" %p)
        txt.write("%d\n" %s)
    else:
        txt.write("%d\n" %p)
        txt.write("%d\n" %s)
        count = 3
        while count <= n:
            termo = p + s
            txt.write("%d\n" %termo)
            s = p
            p = termo
            count += 1
    txt.close()

a = int(input("Quantos termos: "))
fib(a)