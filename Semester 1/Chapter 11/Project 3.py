from datetime import *

# Membuka file dengan mode untuk di baca perbaris
file = open("d:/dataMemberPerpustakaan.txt", "r")

# Read File
read = file.readlines()

# Variable untuk menyimpan waktu saat ini (type=date)
now = datetime.date(datetime.now())

# List untuk menyimpan dictMemberPerpustakaan
dataPerpustakaan = []

# Input Kode Member
cari = input("Masukkan Kode Member : ")

# Looping untuk memanggil data di d:/dataMemberPerpustakaan.txt
for i in range(len(read)):
    data = read[i].rstrip("\n")
    pecahData = read[i].split("|")
    dataDict = {'kode':pecahData[0], 'nama':pecahData[1], 'buku':pecahData[2],'tgl peminjaman':pecahData[3], 'tgl maks peminjaman':pecahData[4], 'tgl pengembalian':now, 'terlambat':0, 'denda':0}
    dataPerpustakaan.append(dataDict)

# Looping untuk mencari data, dan ditampilkan di program
for item in dataPerpustakaan:
    if item['kode'] == cari:
        format = "%Y-%m-%d"
        maks = item['tgl maks peminjaman'].rstrip("\n")
        now = datetime.strptime(now.strftime('%Y-%m-%d'), format)
        datetime_maks = datetime.strptime(maks, format)
        lambat = (now-datetime_maks).days
        if lambat <= 0: lambat = 0; print(f"\nData Peminjaman Buku\nKode Member\t\t\t: {item['kode']}\nNama Member\t\t\t: {item['nama']}\nJudul Buku\t\t\t: {item['buku']}\nTanggal Mulai Peminjaman\t: {item['tgl peminjaman']}\nTanggal Maks Peminjaman\t\t: {item['tgl maks peminjaman']}Tanggal Pengembalian\t\t: {item['tgl pengembalian']}\nTerlambat\t\t\t: {lambat} hari\nDenda\t\t\t\t: Rp. {item['denda']}")
        else: lambat = int(abs(lambat)); denda = lambat*2000; print(f"\nData Peminjaman Buku\nKode Member\t\t\t: {item['kode']}\nNama Member\t\t\t: {item['nama']}\nJudul Buku\t\t\t: {item['buku']}\nTanggal Mulai Peminjaman\t: {item['tgl peminjaman']}\nTanggal Maks Peminjaman\t\t: {item['tgl maks peminjaman']}Tanggal Pengembalian\t\t: {item['tgl pengembalian']}\nTerlambat\t\t\t: {lambat} hari\nDenda\t\t\t\t: Rp. {denda}")
        break
else:
    print("\nData Member tidak ditemukan.")

# # Menutup file
file.close()
