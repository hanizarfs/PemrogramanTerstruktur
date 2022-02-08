def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

alas1 = 10
tinggi1 = 20

alas2 = 15
tinggi2 = 45

print('Luas segitiga pertama dg alas', alas1,
     'dan tinggi', tinggi1,
     'adalah', luasSegitiga(alas1, tinggi1))
print('Luas segitiga kedua dg alas', alas2,
     'dan tinggi', tinggi2,
     'adalah', luasSegitiga(alas2, tinggi2))
