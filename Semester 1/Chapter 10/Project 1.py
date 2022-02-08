# Membuka file dengan mode untuk di baca
file = open("d:/file1.txt", "r")

# Variable
ganjil = 0
genap = 0

# Looping for untuk mengubah type data teks di dalam file, dan memilih ganjil genapnya
for i in file:
    teksIsInt = int(i)
    if teksIsInt%2 == 0:
        genap += 1
    else:
        ganjil += 1

print(f'Banyaknya bilangan genap  : {genap}')
print(f'Banyaknya bilangan ganjil : {ganjil}')

# Menuutp kembali file
file.close()
