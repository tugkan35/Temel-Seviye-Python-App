import random
sayi=random.randint(1,20)
tahmin=int(input("Tahmin et...:"))
skor=100
while True:
    if sayi==tahmin:
        print("Kazandınız..:) Skorunuz...:",skor)
        break
    else:
        print("Olmadı...:( Skorunuz...:",skor)
        skor-=5
        tahmin=int(input("Tahmin et...:"))
