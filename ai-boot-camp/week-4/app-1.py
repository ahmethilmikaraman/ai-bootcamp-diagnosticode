import mysql.connector
from datetime import datetime

#   DATABASE BAĞLANTIMIZI KURALIM  #

connection = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "sql123", 
    database = "bootcampdb")

cursor = connection.cursor()

#  DATABASE'E BİR TABLO EKLEYELİM  #

cursor.execute("CREATE TABLE ogrenciler (id int, ad varchar(40), soyad varchar(15), bolum varchar(60), dogum_tarihi datetime)")

########################################

#   TABLOYA 5 ÖĞRENCİ EKLEYELİM    #

ogrenciler = [
    ("Mehmet", "Kara", "Bilgisayar Mühendisliği", datetime(2006, 2, 14)),
    ("Zeynep", "Demir", "Bilgisayar Mühendisliği", datetime(2005, 11, 3)),
    ("Burak", "Şahin", "Matematik Öğretmenliği", datetime(2004, 9, 22)),
    ("Elif", "Aydın", "Tıp", datetime(2006, 4, 5)),
    ("Kerem", "Yıldız", "Hukuk", datetime(2003, 12, 19))
]

sql = "INSERT INTO ogrenciler(ad,soyad,bolum,dogum_tarihi) VALUES (%s,%s,%s,%s)"

cursor.executemany(sql,ogrenciler)

#############################################

#   BİR ÖĞRENCİNİN BÖLÜM BİLGİSİNİ GÜNCELLEYELİM   #

cursor.execute("UPDATE ogrenciler SET bolum = 'Endüstri Mühendisliği' WHERE id = 2")

#############################################

#   TÜM ÖĞRENCİLERİ LİSTELEYELİM   #

cursor.execute("SELECT * FROM ogrenciler")

results = cursor.fetchall()

for result in results:
    print(result[1],result[2],result[3],result[4])

##############################################

#   BÖLÜM DEĞERİNE GÖRE LİSTELEME YAPALIM   #

cursor.execute("SELECT * FROM ogrenciler WHERE bolum = 'Bilgisayar Mühendisliği'")

results = cursor.fetchall()

for result in results:
    print(result[1],result[2],result[3],result[4])

################################################

#   DOĞUM TARİHLERİNE GÖRE SIRALAMA YAPALIM    #

cursor.execute("SELECT * FROM ogrenciler ORDER BY YEAR(dogum_tarihi), MONTH(dogum_tarihi), DAY(dogum_tarihi)")

results = cursor.fetchall()

for result in results:
    print(result[1],result[2],result[3],result[4])

###
connection.commit()
cursor.close()


