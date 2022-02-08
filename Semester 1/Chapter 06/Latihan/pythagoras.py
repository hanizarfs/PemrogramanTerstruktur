def isPythagoras(a, b, c):
    global hasil
    a = a*a
    b = b*b
    c = c*c
    hasil = (c == a + b)
    if(c == a + b):
        return hasil
    else:
        return hasil

isPythagoras(3, 4, 5)

print('is Pythagoras ?', hasil)
