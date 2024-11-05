savasci = {
    "Güc":200,
    "Can":1500,
    "Zırh":130
}
büyücü = {
    "Güc":250,
    "Can":1400,
    "Zırh":100
}

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["Güc"]-vurulan["Zırh"]
    vurulan["Can"] -= eksilen
print("Savaçşı :",savasci)
print("Büyücü  :",büyücü)

while True:

    input("Vurmak için enter'a basınız!")
    vur(savasci,büyücü)
    print("Savaşçı \U00002694 Büyücüye Saldırdı.")
    print("Savaşçının Can Değeri :",savasci["Can"])
    print("Büyücünün \U0001F494 Can Değeri  :",büyücü["Can"])
    input("Vurmak için enter'a basınız!")

    vur(büyücü, savasci)
    print("Büyücü \U00002694 Savaşçıya Saldırdı.")
    print("Savaşçının \U0001F494 Can Değeri :", savasci["Can"])
    print("Büyücünün Can Değeri  :", büyücü["Can"])

    if savasci["Can"] <=0:
        print("Savaşçı Öldü!!\U0001F480")
        quit()

    if büyücü ["Can"]<=0:
        print("Büyücü Öldü  !!\U0001F480")
        quit()


