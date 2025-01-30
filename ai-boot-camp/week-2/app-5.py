
class Hayvan:
    def make_a_sound(self):
        print("bir hayvan ses çıkarıyor.")

class Kedi(Hayvan):
    def make_a_sound(self):
        print("miyav")
    
class Kopek(Hayvan):
    def make_a_sound(self):
        print("hav hav")


hayvan = Hayvan()
kedi = Kedi()
kopek = Kopek()

hayvan.make_a_sound()
kedi.make_a_sound()
kopek.make_a_sound()

###################################################3

class Araba:
    def __init__(self, marka, model, yil, hiz = 0):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = hiz
    
    def gaza_bas(self):
        self.hiz += 10

    def frene_bas(self):
        if self.hiz > 0 : self.hiz -= 10

    def ibre_goster(self):
        print(f"{self.hiz} km/s")
        input()

    def dur(self):
        print("Araba durduruldu")
        return False
    
    def hakkinda(self):
        print(f"Marka : {self.marka}, Model : {self.model}, Yıl : {self.yil}")
        input()

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, hiz=0, sarj = 100):
        Araba.__init__(self,marka, model, yil, hiz)
        self.sarj = sarj

    def sarj_et(self):
        if self.sarj < 100 : self.sarj = 100 
        else: 
            print("Şarjınız ful.")
            input()

    def pil_seviyesi_göster(self):
        print(f"Pil seviyeniz {self.sarj/20}/5 düzeyinde.")
        input()

        
is_active = True

arac = ElektrikliAraba("Tesla","Model Y0", 2025, 0, 80)

while is_active:
    print("Araba çalıştı")
    print("""
    1- Gaza bas
    2- Frene bas
    3- Şarj et
    4- İbre göster
    5- Pil seviyesi göster
    6- Araba hakkında
    7- Arabayı durdur
-----------------------------------------------
    """)
    secim = int(input("Seçiminiz : "))

    if secim == 1:
        arac.gaza_bas()
    elif secim == 2:
        arac.frene_bas()
    elif secim == 3:
        arac.sarj_et()
    elif secim == 4:
        arac.ibre_goster()
    elif secim == 5:
        arac.pil_seviyesi_göster()
    elif secim == 6:
        arac.hakkinda()
    elif secim == 7:
        is_active = arac.dur()