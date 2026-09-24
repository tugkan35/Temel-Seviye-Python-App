L=[]
while True:
    TC=int(input("TC gir..:"))
    if TC in L:
        i=L.index(TC)
        print("Muayene Sırası..:",i+1)
    elif TC==0:
        print(L[0],'TC numaralı hasta doktorun yanına gidiniz')
        L.pop(0)
    else:
        L.append(TC)
        print(TC,'TC numaralı hasta sıraya alındı')
