import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "sql123", 
    database = "bootcampdb")

cursor = connection.cursor()

cursor.execute("CREATE TABLE dersler (ders_id int, ders_adi varchar(60), kredi int, bolum varchar(60))")

###################################

dersler = [
    ("Algoritma ve Programlama", 5, "Bilgisayar Mühendisliği"),
    ("Veri Yapıları", 6, "Bilgisayar Mühendisliği"),
    ("Bilgisayar Mimarisi", 6, "Bilgisayar Mühendisliği"),
    ("Mühendislik Ekonomisi", 6, "Endüstri Mühendisliği"),
    ("Yöneylem Araştırması", 7, "Endüstri Mühendisliği"),
    ("Anatomi", 7, "Tıp"),
    ("Fizyoloji", 6, "Tıp"),
    ("Patoloji", 7, "Tıp"),
    ("Soyut Cebir", 5, "Matematik Öğretmenliği"),
    ("Medeni Hukuk", 6, "Hukuk"),
    ("Ceza Hukuku", 7, "Hukuk"),
    ("Anayasa Hukuku", 6, "Hukuk")
]

sql = "INSERT INTO dersler(ders_adi,kredi,bolum) VALUES (%s,%s,%s)"

cursor.executemany(sql,dersler)

###################################

#   MANY TO MANY İİLİŞKİ SAĞLANACAĞI İÇİN YENİ BİR TABLO DAHA OLUŞTURALIM   #

cursor.execute("CREATE TABLE ogrenci_bolum (ogrenci_id INT, ders_id INT)")

#  ŞİMDİ BU TABLODA İLİŞKİ SAĞLAYALIM  #

cursor.execute("""
               ALTER TABLE ogrenci_bolum 
               ADD CONSTRAINT fk_ogrenci FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id) ON DELETE CASCADE,
               ADD CONSTRAINT fk_ders FOREIGN KEY (ders_id) REFERENCES dersler(ders_id) ON DELETE CASCADE
               """)

#   İLİŞKİ KURULAN TABLODA OGRENCİLER VE DERSLER ARASI BİLGİLERİ EKLEYELİM  #

sql = "INSERT INTO ogrenci_bolum(ogrenci_id,ders_id) VALUES (%s,%s)"

values = [
    (1,1),
    (1,2),
    (1,3),
    (2,1),
    (2,2),
    (2,3),
    (3,9),
    (4,6),
    (4,7),
    (4,8),
    (5,10),
    (5,11),
    (5,12)
]

cursor.executemany(sql,values)

###################################

#   ÖĞRENCİLERİN ALDIĞI DERSLERİ LİSTELEYEN SORGU   #

cursor.execute("""
               SELECT ogrenciler.ad, ogrenciler.soyad, dersler.ders_adi, dersler.kredi 
               FROM ogrenci_bolum 
               JOIN ogrenciler ON ogrenciler.id=ogrenci_bolum.ogrenci_id 
               JOIN dersler ON dersler.ders_id=ogrenci_bolum.ders_id""")

ogrenciler = cursor.fetchall()

for ogrenci in ogrenciler:
    print(f"{ogrenci[0]} {ogrenci[1]} {ogrenci[3]} kredili {ogrenci[2]} dersini alıyor.")

#    BELİRLİ BİR ÖĞRENCİNİN DERSLERİ     #

cursor.execute("""
               SELECT ogrenciler.ad, ogrenciler.soyad, dersler.ders_adi, dersler.kredi 
               FROM ogrenci_bolum 
               JOIN ogrenciler ON ogrenciler.id=ogrenci_bolum.ogrenci_id 
               JOIN dersler ON dersler.ders_id=ogrenci_bolum.ders_id
               WHERE ogrenciler.id = 3
               """)

ogrenciler = cursor.fetchall()

print(f"{ogrenciler[0][0]} {ogrenciler[0][1]} dersleri")
for ogrenci in ogrenciler:
    print(f"{ogrenci[2]} - {ogrenci[3]} kredi")

###################################

#   KREDİLERİN ORTALAMASINI ALDIK  #

cursor.execute("SELECT AVG(kredi) FROM dersler ")

ortalama = cursor.fetchone()

print(f"ORTALAMA : {ortalama[0]}")

###################################

#   EN YÜKSEK KREDİLİ DERSLERİ SEÇER   #

cursor.execute("SELECT ders_adi, kredi FROM dersler WHERE kredi = (SELECT MAX(kredi) FROM dersler)")

ortalama = cursor.fetchall()

print(ortalama)

###################################

#   BİR ÖĞRENCİ KAYDI SİLME    #

cursor.execute("DELETE FROM ogrenciler WHERE ad = 'Zeynep'")

#   BİR ÖĞRENCİNİN ADINI GÜNCELLEME    #

cursor.execute("UPDATE ogrenciler SET ad = 'Veli' WHERE ad = 'Kerem' ")

connection.commit()

cursor.close()