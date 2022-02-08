# Membuka sekaligus membaca file dengan mode untuk di baca
readFile = open("d:/file5.txt", "r").read()

# Looping for untuk split item di dalam readFile
for i in readFile:
    data = readFile.split("\n")

# List untuk membagi bil1 dan bil2 sekilagus split item
bil1 = [i.split('|')[0] for i in data]
bil2 = [i.split('|')[1] for i in data]

# Membuat item di dalam list menjadi Integer
intBil1 = list(map(int, bil1))
intBil2 = list(map(int, bil2))

# Looping for untuk menjumlahkan kedua item dari masing-masing list, seklaigus di tambhkan kedalam file text
for (item1, item2) in zip(intBil1, intBil2):
    hasil = (item1+item2)
    fil = open("d:/file5_jawaban.txt", "a+")
    fil.write(f'{hasil}\n')
    print(item1+item2)

# Menutup file
file.close()
