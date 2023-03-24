import math
def toplama(a,b):
    print(a+b)

def cikarma(a,b):
    print(a-b)

def carpma(a,b):
    print(a*b)

def bolme(a,b):
    print(a/b)

print("Lütfen yapmak istediğiniz işlemi yazın:")

secim = input("Seçenekler: toplama, çıkarma, çarpma, bölme -> ")
print(secim)

a = float(input("İlk sayı: "))

b = float(input("İkinci sayı: "))

if secim == "toplama":
    toplama(a,b)
elif secim == "çıkarma":
    cikarma(a,b)
elif secim == "çarpma":
    carpma(a,b)
elif secim == "bölme":
    bolme(a,b)
else:
   print("hatalı giriş yaptınız.")
