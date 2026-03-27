########################## GC (Garbarage Collection) #########################
"""
Python değişkenlerin bellek yönetimi otomatik yapılır.
GC: Gereksiz bellek tüketimini engeller
"""

number1 = 44  #Buradaki değer artık çöptür.
number2 = 23


############################## None ###########################################
#None: Python'daki None özel bir veri türüdür ve boş veya tanımsız bir değeri ifade eder.
data = None # tanımsız veya boş anlamına geliyor.
print("Boş değer: ",data)
print(type(data))


############################## Cast ###########################################
# Cast: Type casting yani değişkenlerin Tip dönüşümlerini kullanmak

# int()    : Tam sayıya çevirir.
# float()  : Virgüllü sayıya çevirir.
# str()    : Kelimeye çevirir.
# bool()   : Boolean çevirir.

number2 = "44"
print(type(number2))
print((int(number2)+16))
print((float(number2)+16))

