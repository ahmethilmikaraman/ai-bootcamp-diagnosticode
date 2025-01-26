int_var = 10                #integer
float_var = 3.4             #float
str_var = "diagnosticode"   #string
bool_var = True             #boolean

print(str_var + "is the best group!")
print(int_var + float_var)
print(bool_var and True)
print(str_var + str(int_var))
print(str_var.capitalize())
print(str_var[:4] + "." + str_var[9:])

###################

number_1 = int(input("Sayı giriniz : "))
number_2 = int(input("Sayı giriniz : "))

sum = number_1 + number_2
diff = number_1 - number_2
mult = number_1 * number_2

print(f"""
    Toplam : {sum},
    Fark : {diff},
    Çarpım : {mult}
""")

###################

int_var = 10
float_var = 15.2
str_var = "151515"
bool_var = False

cast_1 = float(int_var)
cast_2 = str(float_var)
cast_3 = int(str_var)
cast_4 = str(bool_var)

print(type(cast_1), cast_1)
print(type(cast_2), cast_2)
print(type(cast_3), cast_3)
print(type(cast_4), cast_4)