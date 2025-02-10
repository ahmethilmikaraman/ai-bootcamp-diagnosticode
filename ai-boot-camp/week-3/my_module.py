def toplama(*sayi):
    """
    Toplama işlemi yapar.
    *toplanacak sayılar
    """
    result = 0
    for i in sayi:
        result += i
    return result

def cikartma(*sayi):
    """
    Çıkartma işlemi yapar
    *çıkarılacak sayılar
    """
    result = 0
    for i in sayi:
        if sayi.index(i) == 0:
            result += i
        else:
            result -= i
    return result

def carpma(*sayi):
    result = 1
    for i in sayi:
        result *= i
    return result

def bolme(*sayi):
    result = sayi[0]
    for i in sayi:
        if sayi.index(i) != 0 and i != 0:
            result /= i
        else:
            print("Hatalı işlem.")

def us_al(sayi, us):
    """
    Üs alma işlemi yapar
    üssü alınacak sayı, üssün kuvveti
    """
    result = sayi
    for i in range(0,us-1):
        result *= sayi
    return result

def oklidUzaklik(point1, point2):
    """
        Öklid Hesabı yapar.
        parametreler =>
        1. nokta konumu , 2. nokta konumu
    """
    return ((((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2)) ** .5)

if __name__ == "__main__":
    print("my_module, bazı matematiksel işlemleri yapmaya yarıyan modüldür.")
