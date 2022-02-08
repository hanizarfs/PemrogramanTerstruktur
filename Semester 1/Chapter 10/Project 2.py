# Membuka file dengan mode untuk di tulis dan dibaca ditambah seek
file = open("d:/file2.txt", "a+")

# Looping while digunakan untuk mengulangi program, jika tidak diminta untuk break
while True:
    nim = input('\nMasukkan NIM      : ')
    nama = input('Masukkan Nama Mhs : ')
    alamat = input('Alamat            : ')
    file.write((f'{nim}|{nama}|{alamat}\n'));
    file.seek(0,0)
    ulangi = input('\nUlangi input lagi [y/n] :')
    if ulangi.lower() not in 'y': break

# Membaca sekaligus mencetak isi filenya
print(f'\n{file.read()}')

# Menutup file
file.close()
