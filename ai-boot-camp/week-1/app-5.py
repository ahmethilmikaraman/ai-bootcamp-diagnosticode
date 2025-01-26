import random

random_number = random.randint(1,10)

guess_num = input("1-10 arası sayı tahmin edin. : ")

if (guess_num == random_number):
    print("Doğru tahmin!")
else:
    print("Yanlış tahmin!")