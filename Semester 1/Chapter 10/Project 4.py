# Membuka file dengan mode untuk di baca perbaris
readFile = (open("d:/file2.txt", "r").readlines())

# Input NIM yang akan di cari
cari = input('Masukkan NIM yang mau dicari : ')

# List untuk menyimpan semua dictionary
dataMhs= []

# Looping for 
for i in range(len(readFile)):
    data = readFile[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataMhs.append(dataDict)
for item in dataMhs:
    if item['nim'] == cari:
        print(f"\nData Mahasiswa\n\nNIM\t: {item['nim']}\nNama\t: {item['nama']}\nAlamat\t: {item['alamat']}")
        break
else:
    print("\nData mahasiswa tidak ditemukan.")

# Menutup file
file.close()
