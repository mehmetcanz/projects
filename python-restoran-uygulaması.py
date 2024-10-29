masalar=dict()
for a in range(20):
    masalar[a]=0

def hesap_ekle():
    masa_no = int(input("Masa Numarası : "))
    bakiye = masalar[masa_no]
    eklenecek_ücret=float(input("Eklenecek Ücret : "))
    guncel_bakiye= bakiye + eklenecek_ücret
    masalar[masa_no] = guncel_bakiye
    print("İşlem Tamamlandı.")

def hesap_odemesi():
    masa_no = int(input("Masa Numarası : "))
    bakiye = masalar[masa_no]
    print("Masa {} 'in hesabı : {}".format(masa_no,bakiye))
    masalar[masa_no] = 0
    print("Hesap Ödendi. \U00002705")

def dosya_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi,"r",encoding="utf-8")
        veri=dosya.read()
        veri=veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]]=float(a[1])
    except FileNotFoundError:
        dosya=open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("Kayıt Dosyası Oluşturuldu.")

def dosya_guncelle(dosya_adi):
    dosya=open(dosya_adi,"w",encoding="utf-8")
    for a in range(20):
        bakiye = masalar[a]
        bakiye=str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()


def ana_islemler():
    dosya_kontrolu("Bakiye.txt")
    while True:
        print("""
            Mehmet Can Zorlu Restaurant Uygulaması        
        1-) Masaları Görüntüle :
        2-) Hesap Ekleme :
        3-) Hesap Ödeme : 
        Q-) Çıkış
        
        """)
        secim=input("Yapılacak İşlem : ")
        if secim=="1":
            for a in range(20):
                print("Masa {} için hesap: {} ".format(a,masalar[a]))

        elif secim=="2":
            hesap_ekle()

        elif secim== "3" :
            hesap_odemesi()

        elif secim=="q" or secim=="Q":
            print("Çıkış Yapıldı.")
            quit()
        else:
            print("Hatalı Seçim Yaptınız.")
            dosya_guncelle("Bakiye.txt")
        input("Ana Menüye Dönmek İçin ENTER'a Basın.")

ana_islemler()
