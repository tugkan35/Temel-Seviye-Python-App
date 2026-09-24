import random
Liste = ["Taş","Kağıt","Makas"]
pc=random.choice(Liste) # bilgisayarın liste içerisinden rastgele seçimi
player=input('[Taş-Kağıt-Makas]:').capitalize() # kullanıcının liste içerisinden rastgele seçimi

print("Bilgisayar ",pc," seçti")
print("sen ",player," seçtin")

if pc==player:
    print("Berabere")
if pc=="Kağıt" and player=="Taş":
    print("Kaybettin")
if pc=="Taş" and player=="Makas":
    print("Kaybettin")
if pc=="Makas" and player=="Kağıt":
    print("Kaybettin")

if pc=="Kağıt" and player=="Makas":
    print("Kazandın..")
if pc=="Taş" and player=="Kağıt":
    print("Kazandın..")
if pc=="Makas" and player=="Taş":
    print("Kazandın..")
else:
    print("Liste dışı giriş yaptınız...!")
