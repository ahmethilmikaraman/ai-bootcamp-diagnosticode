
def append_data(text):
    file = open("week-3\data.txt","a", encoding='utf-8')
    file.write(text + "\n")
    file.close()

def display_data():
    try:
        file = open("week-3\data.txt", "r", encoding= 'utf-8')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("dosyanız bulunmamaktadır.")
    finally:
        file.close()


while True:
    selection = int(input("""
Dosyanıza hangi işlemi yapmak istersiniz?

1-Yeni veri ekle.
2-Dosyayı oku.
3-Çıkış yap.

Seçiminiz : """))
    
    print("\n")

    if selection in [1,2,3]:
        if selection == 3:
            print("Çıkış yapıldı.")
            break
        if selection == 1:
            data = input("""
Eklenecek veri:
""") 
            append_data(data)
        if selection == 2:
            display_data()


##########################################################

import json

data = {
    "kisiler": [
        {
            "ad": "Ahmet",
            "yas": 25,
            "sehir": "İstanbul"
        },
        {
            "ad": "Hilmi",
            "yas": 30,
            "sehir": "Ankara"
        }
    ]
}



with open("week-3\kisiler.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

with open("week-3\kisiler.json", "r", encoding="utf-8") as file:
    content = json.load(file)
    print(content)
    content["kisiler"][0]["sehir"] = "Usak"

with open("week-3/kisiler.json", "w", encoding="utf-8") as file:
    json.dump(content, file)

