import random
Liste= ["python","print","random","while","choice"]
kelime = random.choice(Liste)
adam = ['''
   +----+
   o    |
 / | \  |
  / \   |
       ---''','''
   +----+
   o    |
 / | \  |
  /     |
       ---''','''
   +----+
   o    |
 / | \  |
        |
       ---''','''
   +----+
   o    |
 / |    |
        |
       ---''','''
   +----+
   o    |
   |    |
        |
       ---''','''
   +----+
   o    |
        |
        |
       ---''','''
   +----+
        |
        |
        |
       ---''']

dogruHarf=[]
yanlısHarf=[]
hak=len(adam)

while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
    if out == kelime:
        break
    print("kelime: ",out)
    print(adam[hak-1])
    girHarf=input()
    if girHarf in dogruHarf or girHarf in yanlısHarf:
        print(girHarf,"Zaten girildi")
    elif girHarf in kelime:
        print ("doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("Yanlış Harf..!")
        hak-=1
    yanlısHarf.append(girHarf)

if hak!=0:
    print("Tebrikler.. Kazandınız.. Kelimeniz : ",kelime)
else:
    print("Malesef... Kaybettin.. Kelime : ",kelime,"idi")
