# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
 
indeks  = kilo/(boy*boy)
 
if indeks <18:
    print("\n zayıfsınız vücut kitle indeksiniz:{}".format(indeks))
elif indeks >= 18 and indeks <25 :
    print("\n normalsiniz vücut kitle indeksiniz:{}".format(indeks))
elif indeks >= 25 and indeks <30:
    print("\n kilolusunuz vücut kitle indeksiniz:{}".format(indeks))
elif indeks >= 30 and indeks <35:
    print("\n obezsiniz vücut kitle indeksiniz:{}".format(indeks))
else:
    print("\n ciddi obezsiniz vücut kitle indeksiniz:{}".format(indeks))

  #2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = int(input("Lütfen birinci sayıyı giriniz:"))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz:"))
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz:"))
 
enBuyukSayı = max (sayi1, sayi2, sayi3)
 
print ("Girilen en büyük sayı: ", enBuyukSayı)

#4 Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
r=int(input("Yarı Çapı Girin: "))
cevre=2*3.14*r
alan=3.14*r*r
print("Çevre: ",cevre)
print("Alan: ",alan)

#5 Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Lütfen bir sayı giriniz:")
tersi=sayi[::-1]
if tersi == sayi:
    print('Girilen sayı palindromdur')
else:
    print('Girilen sayı palindrom değildir.')

