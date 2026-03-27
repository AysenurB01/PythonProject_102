#pylint: disable=C0114
""" """

# Python dinamik türlü Yüksek seviyeli interpreter bir dildir.
# Değişken türleri genel kurallar (Common Rules)
# Değişken isimlendirmelerde: _(under score)
# snake_case

############################## LIST ##################################
#type=list
my_list1 = [1,2,3,4,"Malatya"]
my_list2 = [5,6,7,8,True,"Adana",14,53]
print(f"list1: {my_list1}")
print(f"list2: {my_list2}")
print(type(my_list1))


############################## TUPLE ##################################
#liste yapısına çok benzer bunda sadece immutable(değişmez)
# type=tuple
my_tuple = (1,2,3,4,"Malatya")
print(f"my_tuple: {my_tuple}")
print(type(my_tuple))


############################## SET ####################################
# Set : Aynı verilerden sadece bir tane gösterir.
my_set = (1,1,1,2,3,4,"Malatya")
print(f"my_set: {my_set}")
print(type(my_set))


############################## DICTIONARY (SÖZLÜK) #####################
# type=dict
person = {
    "name":"Ayşe",
    "surname":"Büyümez",
    "is_login": True,
    "hes_code":1456621545
}
print(person)
print(type(person))
