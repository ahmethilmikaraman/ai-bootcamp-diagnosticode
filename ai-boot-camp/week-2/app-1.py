
def mean(array):
    return sum(array) / len(array)     

arrayOfNumber = [15,32,1,83,44,72,44,28,72,5,90]

result = mean(arrayOfNumber)

print(result)

#############################################

def show_bigger(num1, num2):
    if num1 > num2 : return num1
    else : return num2

print(f"""
    {show_bigger(15,32)}
    {show_bigger(7,3)}
    {show_bigger(75,75)}
        """)


##############################################

def count_word(sentence, mark = " "):
    return len(sentence.split(mark))

sentence1 = "Sabah erkenden kalkıp kitap okudum, sonra kahvaltı yaptım."
sentence2 = "Bugün derse giderken yağmur yağmaya başladı ama yanımda şemsiye yoktu."
sentence3 = "Bilgisayar/mühendisliği,/matematik,/fizik/gibi/alanlarla/ilgileniyorum."

print(f"""
    {count_word(sentence1)}
    {count_word(sentence2)}
    {count_word(sentence3, "/")}
        """)


