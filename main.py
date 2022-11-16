print("Merhaba Etiya")
#string : metinler  "" kullanılır
text = "cemre"
print(text)
baslik = "HABERİNİZ OLSUN"
print(baslik)
print(type(baslik))
# integer : tam sayı
number = 10
print(number)
# float : ondalıklı sayı virgül kullanılmaz
dnumber = 7.2
print(dnumber)
# boolean : True , False
# matematiksel operatörler
print(number + 10)
print(number - 10)
print(number * 10)
print(number / 10)
print(number % 10) # mod bölümde kalanı verir
# mantıksal operatörler
print(1==2)
print(1!=2)
print(1>2)
print(1<2)
print(1<=2)
print(1>=2)
print(10%2==0)
print(50/2==25)
print(50/2==25.0)
# string fonksiyonları
text = 'Merhaba Etiya'
print(text.upper()) # Metni buyuk yazar
print(text.lower()) # Metni kucuk yazar
print(text.startswith("Mev")) # Cümle basi ... ile basliyor mu?
print(text.endswith("Etiya")) # Cümle sonu ... ile bitiyor mu?
# f string
name = 'cemre'
age = 26
company = 'Etiya'
print(f"{name} {age} yasinda {company}'da calisiyor")