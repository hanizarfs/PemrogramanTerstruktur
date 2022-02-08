# Projcet 7

try:
    filename = input("Path File  : ")
    teksSandi = open(filename, "r").read()
    n = int(input('Nilai N    : '))
    
    print(f'\nTeks Sandi : {teksSandi}')
    teksAsli = ''
    for i in teksSandi:
        value = ord(i)
        newValue = value-n
        if newValue == 30:
            newValue = 32
        elif newValue < 65:
            newValue = 90 - (64-newValue)
        teksAsli += (chr(newValue))
    file = open("d:/file7_dekripsi.txt", "a+")
    file.write(f'{teksAsli}')
    print(f'Teks Asli  : {teksAsli}')
    file.close()
    
except FileNotFoundError:
    print('File tidak ditemukan')
except PermissionError:
    print('File tidak ditemukan') 
