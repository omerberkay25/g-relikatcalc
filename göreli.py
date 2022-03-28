from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import göreli_win as göreli

#  X DOĞRULTUSU


class StoryDrift_Check(QtWidgets.QMainWindow):
    def __init__(self):
        super(StoryDrift_Check, self).__init__()
        self.ui = göreli.Ui_Form()
        self.ui.setupUi(self)
    
    
    
    
    
    # DEPREM PARAMETRELERİ
    R = float(input("R Değerini Giriniz: "))
    I = float(input("I Değerini Giriniz: "))
    Kappa = float(input("κ Değerini Giriniz: "))
    Tp = float(input("Tp Değerini Giriniz: "))
    hi = float(input("hi değerini giriniz: "))
    xdeplasman = float(input("x deplasman: "))
    binaonem = float(input("Bina Önem Katsayısı: "))
    celikcerceve = input("Evet veya Hayır Giriniz: ")
    esnekduvar = input("Yok veya Var Giriniz: ")

    #DD-2 Parametreleri
    sdsfordd2 = float(input("DD2 için SDS: "))
    sd1fordd2 = float(input("DD2 için SD1: "))

    #DD-3 Parametreleri
    sdsfordd3 = float(input("DD3 için SDS: "))
    sd1fordd3 = float(input("DD3 için SD1: "))

    Δi_hi = float(xdeplasman/hi)


    # if (Tp<sd1fordd2/sdsfordd2):
    #     lambda1 = sdsfordd3/sdsfordd2
    #     kontrol = lambda1*Δi_hi*R/I
        
    # elif (Tp<sdsfordd3/sdsfordd2):
    #     lambda2 =sd1fordd3/sd1fordd2
    #     kontrol = lambda2*Δi_hi*R/I
    # else:
    #     print("Geçersiz değer girildi")


    if (esnekduvar == "Var" and celikcerceve == "Hayır"):
        case1 = (0.016*Kappa)
        print(case1)
        print(Δi_hi)
        if (Tp<sd1fordd2/sdsfordd2):
            lambda1 = sdsfordd3/sdsfordd2
            kontrol = lambda1*Δi_hi*R/I
            print(kontrol)
            if case1 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
        
        elif (Tp<sdsfordd3/sdsfordd2):
            lambda2 =sd1fordd3/sd1fordd2
            kontrol = lambda2*Δi_hi*R/I
            print(kontrol)
            if case1 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
        
    elif (esnekduvar == "Var" and celikcerceve == "Evet"):
        case2 = (0.016*Kappa*1.5)
        print(case2)
        print(Δi_hi)
        if (Tp<sd1fordd2/sdsfordd2):
            lambda1 = sdsfordd3/sdsfordd2
            kontrol = lambda1*Δi_hi*R/I
            print(kontrol)
            if case2 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı") 
        elif (Tp<sdsfordd3/sdsfordd2):
            lambda2 =sd1fordd3/sd1fordd2
            kontrol = lambda2*Δi_hi*R/I
            print(kontrol)
            if case2 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
    elif (esnekduvar == "Yok" and celikcerceve == "Hayır"):
        case3 = (0.08*Kappa)
        print(case3)
        print(Δi_hi)
        if (Tp<sd1fordd2/sdsfordd2):
            lambda1 = sdsfordd3/sdsfordd2
            kontrol = lambda1*Δi_hi*R/I
            print(kontrol)
            if case3 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
        
        elif (Tp<sdsfordd3/sdsfordd2):
            lambda2 =sd1fordd3/sd1fordd2
            kontrol = lambda2*Δi_hi*R/I
            print(kontrol)
            if case3 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
        
        
    elif (esnekduvar == "Yok" and  celikcerceve == "Evet"):
        case4 = (0.08*Kappa*1.5)
        print(case4)
        print(Δi_hi)
        if (Tp<sd1fordd2/sdsfordd2):
            lambda1 = sdsfordd3/sdsfordd2
            kontrol = lambda1*Δi_hi*R/I
            print(kontrol)
            if case4 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
        elif (Tp<sdsfordd3/sdsfordd2):
            lambda2 =sd1fordd3/sd1fordd2
            kontrol = lambda2*Δi_hi*R/I
            print(kontrol)
            if case4 > kontrol:
                print("Göreli Kat Ötemeleri Tüm Katlarda Sağlamaktadır")
            else:
                print("Taşıyıcı Sistemin Rijitliği Artırılmalı")
    else:
        ("Hatalı giriş yaptınız")


def app():
    app = QtWidgets.QApplication(sys.argv)
    window = StoryDrift_Check()
    window.show()
    sys.exit(app.exec_())

app()
