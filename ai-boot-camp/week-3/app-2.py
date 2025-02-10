
def bölme(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Bir sayi 0'a bölünemez."

number1 = int(input("1. sayıyı giriniz : "))
number2 = int(input("2. sayıyı giriniz : "))

print(bölme(number1,number2))

########################################################

class NegativeNumberError:
    def __init__(self, num):
        if num < 0:
            raise Exception("Negatif Değer!")

number = int(input("Sayı gir : "))

try:
    hata = NegativeNumberError(number)
    print(number)
except Exception as ex:
    print(ex)