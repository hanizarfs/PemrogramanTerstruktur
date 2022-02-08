def luasSegitiga(a, t):
    global luas
    luas = a * t / 2
    return luas

alas1 = 10
tinggi1 = 20

alas2 = 15
tinggi2 = 45

print('Luas segitiga pertama dg alas', alas1,
     'dan tinggi', tinggi1,
     'adalah', luasSegitiga(10, 20))
luas1 = luas
print('Luas segitiga kedua dg alas', alas2,
     'dan tinggi', tinggi2,
     'adalah', luasSegitiga(15, 45))
luas2 = luas
jumlah = (luas1 + luas2)
print('Jumlah kedua luas tersebut adalah ' + str(jumlah))
