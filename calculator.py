sayi1 = float (input ("1. Sayı >>"))
sayi2 = float (input ("2. Sayı >>"))
islem = input ("İşlemi giriniz (+,-,*,/) >>")

if islem == "+" :
    sonuc = sayi1 + sayi2
    print (sonuc)

elif islem == "-" :
        sonuc = sayi1 - sayi2
        print(sonuc)

elif islem == "*":
        sonuc = sayi1 * sayi2
        print(sonuc)


elif islem == "/"and sayi2 != 0:
    sonuc = sayi1 / sayi2
    print(sonuc)


else:
    print("Hatalı giriş yaptınız...")

input("ENTER tuşuna basarak çıkış yapabilirsiniz...")

