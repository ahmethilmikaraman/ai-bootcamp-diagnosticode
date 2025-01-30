

class HesapMakinesi:
    def topla(self, n1, n2):
        return n1 + n2

    def cikar(self, n1, n2):
        return n1 - n2
    
    def carp(self, n1, n2):
        return n1 * n2
    
    def bol(self, n1, n2):
        return n1 / n2
    
hesaplayici = HesapMakinesi()

print(f"""
    {hesaplayici.topla(10, 5)}
    {hesaplayici.cikar(10, 5)}
    {hesaplayici.carp(10, 5)}
    {hesaplayici.bol(10, 5)}
    """)


####################################################

class Ogrenci:
    def __init__(self,name, notes, degree):
        self.name = name
        self.notes = notes
        self.degree = degree

    def calculate_mean(self):
        return sum(self.notes) / len(self.notes)
        
ogrenci1 = Ogrenci("ahmet", [100, 85, 95, 75], "8. sınıf")
ogrenci2 = Ogrenci("mehmet", [35, 75, 55, 100], "7. sınıf")
ogrenci3 = Ogrenci("ipek", [90, 75, 55, 45], "11. sınıf")

print(f"""
    Öğrenci not ortalamaları
    ----------------------
    {ogrenci1.name} : {ogrenci1.calculate_mean()},
    {ogrenci2.name} : {ogrenci2.calculate_mean()},
    {ogrenci3.name} : {ogrenci3.calculate_mean()},

    """)