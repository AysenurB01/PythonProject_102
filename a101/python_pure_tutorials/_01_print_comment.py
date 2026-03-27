# Single Comment

"""
Multiple Comment
"""

# ===================================
# PRINT
# ===================================

print("Python Öğreniyorum")

print("Python", "Java", "Nodejs")
print("Python" "Java" "Nodejs")
# print("Python" "Java" "Nodejs")  YAZAMAYIZ

# Tam sayı
print(1453)

# Floating Point
print(14,53)
print(14.53)

# ===================================
# SEPERATE
# ===================================
print("Merhabalar", "Güzel", "İnsanlar",sep=" * ")

# ===================================
# END
# ===================================
print("Merhabalar", "Python", "Öğreniyorum", "***", "Dünyasına hoşgeldiniz")
print("Merhabalar", "Python", "Öğreniyorum", end=" *** ")
print("Dünyasına hoşgeldiniz")

# ===================================
# DOCSTRING
# ===================================
print("""
Merhabalar Python Öğreniyorum *** Dünyasına hoşgeldiniz""")

# ===================================
# ESCAPE CHARACTER (\)   \n=new  \t=tab Formating
# ===================================
print("""
Merhabalar Python Öğreniyorum *** \n\tDünyasına hoşgeldiniz""")


# =============================================
# NON-ESCAPE CHARACTER(\) raw String(Ham String)
# r: escape character(r devre dışı bırakmak için kullanıyoruz.)
# =============================================
print("C:\\User\\AppData")
print(r"C:\\User\\AppData")


# ===================================
# VARIBLE
# ===================================
# Değişken isimlendirmelerde
name = "Ayşe"
surname = "Büyümez"

# print("Adım: ",name, \nSoyisim: ",surname)

#1.Yol
print("Adım: ",name, " Soyisim: ",surname)

#2.Yol (%s:decimal(tam sayılar)  %f: float(virgüllü sayılar))
print("Adım: %s Soyisim: %s "%(name, surname))

#3.Yol
print(f"Adım:  {name}, Soyisim:  {surname}")