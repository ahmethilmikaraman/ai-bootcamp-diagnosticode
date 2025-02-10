import math

def hesap_makinesi():
    print("""
Hesap Makinesi
          
1. Toplama
2. Çıkarma
3. Çarpma          
4. Bölme
5. Üs Alma
6. Karekök Alma
7. Logaritma (10 tabanında)
8. Çıkış
          """)
    
    while True:
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-8): ")
        
        if secim == '8':
            print("Hesap makinesinden çıkılıyor...")
            break
        
        if secim in ['1', '2', '3', '4', '5']:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            
            if secim == '1':
                print(f"Sonuç: {sayi1 + sayi2}")
            elif secim == '2':
                print(f"Sonuç: {sayi1 - sayi2}")
            elif secim == '3':
                print(f"Sonuç: {sayi1 * sayi2}")
            elif secim == '4':
                if sayi2 == 0:
                    print("Hata: Sıfıra bölme hatası!")
                else:
                    print(f"Sonuç: {sayi1 / sayi2}")
            elif secim == '5':
                print(f"Sonuç: {math.pow(sayi1, sayi2)}")
        
        elif secim == '6':
            sayi = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
            if sayi < 0:
                print("Hata: Negatif sayıların karekökü alınamaz!")
            else:
                print(f"Sonuç: {math.sqrt(sayi)}")
        
        elif secim == '7':
            sayi = float(input("Logaritmasını almak istediğiniz sayıyı girin: "))
            if sayi <= 0:
                print("Hata: Logaritma yalnızca pozitif sayılar için tanımlıdır!")
            else:
                print(f"Sonuç: {math.log10(sayi)}")
        
        else:
            print("Geçersiz giriş! Lütfen 1-8 arasında bir sayı girin.")
        
        print("\n")

hesap_makinesi()

################################################################################################

import my_module as my

print(help(my))
print(help(my.oklidUzaklik))

print(my.toplama(10,4,7))
print(my.cikartma(2,4))
print(my.carpma(2,5))
print(my.us_al(3,4))
print(my.oklidUzaklik((3,5),(5,7)))

