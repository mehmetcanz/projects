import os

class Musteri():
    def __init__(self,TC,ISIM,SIFRE):
        self.tc = TC
        self.isim = ISIM
        self.sifre = SIFRE
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,TC,ISIM,SIFRE):
        self.musteriler.append(Musteri(TC,ISIM,SIFRE))
        print("İnternet bankacılığına kayıt olduğunuz için teşekkür ederiz :)")

banka = Banka()
menu = "Ana Menüye dönmek için enter'a basınız."
while True:
    os.system("cls")
    print("""
                MEMOBANK'a Hoş Geldiniz
            
            1) Müşteriyim
            2) Müşteri Olmak İstiyorum
            Q) Çıkış
            
    """)
    secim = input("Seçim Yapınız : ")
    if secim=="1":
        girilen_tc = input("TC No Giriniz : ")
        tc_no = [a.tc for a in banka.musteriler]
        if girilen_tc in tc_no:
            for musteri in banka.musteriler:
                if girilen_tc==musteri.tc:
                    girilen_sifre = input("Şifrenizi giriniz : ")
                    if girilen_sifre==musteri.sifre:
                        while True:
                            os.system("cls")
                            print("""
                                    Hoş Geldiniz Sayın {}
                                    
                                1) Bakiye Sorgula
                                2) Para Yatır
                                3) Para Transfer Et
                                4) Para Çek
                                Q) Çıkış
                            """.format(musteri.isim))
                            secim2 = input("İşlem numarası giriniz : ")
                            if secim2 == "1":
                                print("Bakiyeniz : {} ".format(musteri.bakiye))
                                input(menu)
                            elif secim2 == "2":
                                yatirilan_tutar = int(input("Miktar : "))
                                onay = input("Kendi hesabınıza {} TL para yatırmayı onaylıyor musunuz? (E/H)  : ".format(yatirilan_tutar))
                                if onay=="e" or onay=="E":
                                    musteri.bakiye += yatirilan_tutar
                                    print("Paranız yatırıldı.")
                                    input(menu)
                                elif onay=="h" or onay=="H":
                                    print("İşlem iptal edildi.")
                                    input(menu)
                                else:
                                    print("Hatalı seçim yaptınız.")
                                    input(menu)
                            elif secim2 == "3":
                                hedef_TC = input("Yatırılacak Hesabın TC : ")
                                if hedef_TC in tc_no:
                                    for musteri2 in banka.musteriler:
                                        if hedef_TC == musteri2.tc:
                                            yatirilan_tutar2 = int(input("Miktar : "))
                                            if yatirilan_tutar2 <= musteri.bakiye:
                                                onay=input("{} adlı müşterimize, {} TL tutarında parayı göndermeyi onaylıyor musunuz? (E/H)   : ".format(musteri2.isim,yatirilan_tutar2))
                                                if onay == "e" or onay == "E":
                                                    musteri2.bakiye += yatirilan_tutar2
                                                    musteri.bakiye -= yatirilan_tutar2
                                                    print("Paranız yatırıldı.")
                                                    input(menu)
                                                elif onay == "h" or onay == "H":
                                                    print("İşlem iptal edildi.")
                                                    input(menu)
                                                else:
                                                    print("Hatalı seçim yaptınız.")
                                                    input(menu)
                                            else:
                                                print("Bakiyeniz yetersiz!")
                                                input(menu)
                                else:
                                    print("Müşteri bulunamadı!")
                                    input(menu)
                            elif secim2 == "4":
                                cekilecek_tutar = int(input("Miktar : "))
                                if cekilecek_tutar <= musteri.bakiye:
                                    musteri.bakiye -= cekilecek_tutar
                                    print("İşlem tamamlandı.")
                                    input(menu)
                                else:
                                    print("Bakiyeniz yetersiz!")
                                    input(menu)
                            elif secim2 == "Q" or secim2 == "q":
                                print("Hesabınızdan çıkış yapılıyor.")
                                input(menu)
                                break
                            else:
                                print("Hatalı seçim yaptınız.")
                                input(menu)
    elif secim=="2":
        t = input("TC giriniz : ")
        i = input("İsim giriniz : ")
        s = input("Şifre giriniz : ")
        banka.musteri_ol(t,i,s)
        input(menu)
    elif secim=="q" or secim=="Q":
        print("Çıkış yapılıyor. Yine bekleriz.")
        quit()
    else:
        input(menu)
