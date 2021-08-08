import random
secenek = ["taş", "kağıt", "makas"]
taş = secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print ("Taş kağıt makasa hoş geldiniz\n Oyunu bitirmek için f tuşuna basınız")

while True:
    secim = input ("Taş mı kağıt mı makas mı?")
    bil_secim=random.choice(secenek)
    if secim == taş :
        if bil_secim == taş:
            print ("Bilgisayarın seçimi taş,\n Sonuç : Berabere")
        elif bil_secim == kağıt:
            print ("Bilgisayarın seçimi kağıt, \n Sonuç : Kaybettiniz")
        else:
            print ("Bilgisayarın seçimi makas, \n Sonuç : Kazandınız")


    if secim == kağıt:
        if bil_secim == taş:
            print("Bilgisayarın seçimi taş,\n Sonuç : Kazandınız")
        elif bil_secim == kağıt:
            print("Bilgisayarın seçimi kağıt, \n Sonuç : Berabere")
        else:
            print("Bilgisayarın seçimi makas, \n Sonuç : Kaybettiniz")


    if secim == makas:
        if bil_secim == taş:
            print("Bilgisayarın seçimi taş,\n Sonuç : Kaybettiniz")
        elif bil_secim == kağıt:
            print("Bilgisayarın seçimi kağıt, \n Sonuç : Kazandınız")
        else:
            print("Bilgisayarın seçimi makas, \n Sonuç : Berabere")
    if secim == "f" :
                print ("Çıkılıyor...")
                break
