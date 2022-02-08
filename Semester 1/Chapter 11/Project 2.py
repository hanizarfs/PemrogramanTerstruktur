from datetime import *

# Membuka file, dengan mode a+ (dibaca dan ditulis)
file = open("d:/dataMemberPerpustakaan.txt", "a+")

# Variable untuk menyimpan waktu saat ini
now = datetime.date(datetime.now())

# Variable untuk menyatakan maksimal pengembalian
maks = datetime.date(datetime.now()) + timedelta(days=7)

# Looping untuk input data
while True:
    kode, nama, buku = input("\nMasukkan Kode Member : "), input("Masukkan Nama Member : "), input("Masukkan Judul Buku  : ")
    file.write((f'{kode}|{nama}|{buku}|{now}|{maks}\n'))
    again = input("\nUlangi lagi (y/n) ? : ")
    if again.lower() != 'y': break

# Menutup file
file.close()
