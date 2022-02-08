def luasSegitiga2(a, t):
    luas = a * t / 2
    print('Luas segitiga dg alas', a,
     'dan tinggi', t,
     'adalah', luas)
    list_luas.append(luas)
    jml_luas =sum(list_luas)
    print('Jumlah kedua luas tersebut adalah : ' +str(jml_luas))
    
alas = 10, 15
tinggi = 20, 45
list_luas = []
luasSegitiga2(10, 20)
luasSegitiga2(15, 45)
